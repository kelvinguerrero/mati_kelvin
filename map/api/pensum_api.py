from map.models import Pensum, Master
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.pensum_common import list_pensums
import json


@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def pensum(request, pensum_id=None):

    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'),status=500)
    else:
        if (request.method == 'GET'):
            if (pensum_id == None):
                response = list_pensums()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                pensum = Pensum.objects.get(id=pensum_id)
                json_response = json.dumps(pensum.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST
            if validate_data(data, attrs=['name', 'active', 'master_id']):
                master_obj = Master.objects.get(id=data['master_id'])
                pensum = Pensum.objects.create(name=data['name'], active=data['active'], master=master_obj)

                json_response = json.dumps(pensum.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)

        elif request.method == 'PUT':
            data = request.DATA

            if pensum_id != None:
                pensum = Pensum.objects.get(id=pensum_id)

                if 'name' in data:
                    pensum.name = data['name']
                if 'active' in data:
                    if data['active'] == 'True':
                        pensum.active = True
                    elif data['active'] == 'False':
                        pensum.active = False
                pensum.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)

        elif request.method == 'DELETE':
            if pensum_id != None:
                pensum = Pensum.objects.get(id=pensum_id)
                pensum.active = False
                pensum.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        return HttpResponse(status=400)