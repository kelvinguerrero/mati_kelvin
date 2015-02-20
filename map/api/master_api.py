from map.models import Master
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.master_common import list_masters
import json


@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def master(request, master_id=None):

    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'), status=500)
    else:
        if (request.method == 'GET'):
            if (master_id == None):
                response = list_masters()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                master = Master.objects.get(id=master_id)
                json_response = json.dumps(master.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST
            if validate_data(data, attrs=['name']):
                master = Master.objects.create(name=data['name'])

                json_response = json.dumps(master.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)

        elif request.method == 'PUT':
            data = request.DATA
            if master_id != None:
                master = Master.objects.get(id=master_id)

                if 'name' in data:
                    master.name = data['name']

                master.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)

        elif request.method == 'DELETE':
            if master_id != None:
                master = Master.objects.get(id=master_id)
                if not master == None:
                    master.delete()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        return HttpResponse(status=400)