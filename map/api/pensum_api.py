from map.models import Pensum
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.pensum_common import list_pensums
import json


@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def pensum(request, pensum_id=None):

    if (request.method == 'GET'):
        if (pensum_id == None):
            response = list_pensums()
            json_response = json.dumps(response)

            return HttpResponse(json_response,status=200,content_type='application/json')
        else:
            pensum = Pensum.objects.get(id=pensum_id)
            json_response = json.dumps(pensum.to_dict())
            return HttpResponse(json_response,status=200,content_type='application/json')
    elif request.method == 'POST':
        data = request.POST

        if validate_data(data, attrs=['name']):
            pensum = Pensum.objects.create(name=data['name'])
            json_response = json.dumps(pensum.to_dict())
            return HttpResponse(json_response,status=200,content_type='application/json')
        else:
            return HttpResponse(status=500)
    elif request.method == 'PUT':
        data = request.DATA
        if pensum_id != None:
            pensum = Pensum.objects.get(id=pensum_id)

            if 'name' in data:
                pensum.name = data['name']
            if 'active' in data:
                pensum.active = data['active']

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