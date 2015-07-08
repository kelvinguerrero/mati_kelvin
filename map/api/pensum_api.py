# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'

from django.views.decorators.csrf import csrf_exempt
from map.models import Pensum, Master
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.pensum_common import list_pensums, dar_cursos_pensum, agregar_curso
from map.common.error_common import error_json
import json

@csrf_exempt
@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def pensum(request, pensum_id=None):

    # if not request.user.is_authenticated():
    #     return HttpResponse(unicode('Usuario sin autenticacion'),status=500)
    # else:
        if (request.method == 'GET'):
            if (pensum_id == None):
                response = list_pensums()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                data = request.GET
                if validate_data(data, attrs=['operation']):
                    if "operation" in data:
                        if data['operation'] == "1":
                            if pensum_id == None:
                                return HttpResponse(unicode('Se debe agregar el id del pensum'), status=500)
                            response = dar_cursos_pensum(pensum_id)
                            json_response = json.dumps(response)
                            if response != None :
                                return HttpResponse(json_response, status=200, content_type='application/json')
                            else:
                                error = error_json(2, "No existe plan de estudios")
                                return HttpResponse(error, status=500, content_type='application/json')
                        else:
                            error = error_json(4, "No existe la operación")
                            return HttpResponse(error, status=500,content_type='application/json')
                    else:
                        pensum = Pensum.objects.get(id=pensum_id)
                        json_response = json.dumps(pensum.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.DATA
            if validate_data(data, attrs=['operation', 'name', 'active', 'master_id']):
                    master_obj = Master.objects.get(id=data['master_id'])
                    print("ENTRI"   )
                    pensum = Pensum.objects.create(name=data['name'], active=data['active'], master=master_obj)

                    json_response = json.dumps(pensum.to_dict())
                    return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)

        elif request.method == 'PUT':
            data = request.DATA
            if pensum_id!=None:
                if validate_data(data, attrs=['name', 'active', 'operation', 'code_course', 'summer', 'name', 'credits']):
                    if 'operation' in data:
                        if data['operation'] == "1":
                            codigo_curso = data['code_course']
                            summer = data['summer']
                            name = data['name']
                            credits = data['credits']

                            obj_curso = agregar_curso(id_pensum=pensum_id,
                                                      code=codigo_curso,
                                                      summer=summer,
                                                      name=name,
                                                      credits=credits
                                                      )
                            json_response = json.dumps(obj_curso.to_dict())
                            return HttpResponse(json_response, status=200, content_type='application/json')
                    else:
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