# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'

from django.views.decorators.csrf import csrf_exempt
from map.models import Master
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.error_common import error_json
from map.common.report_common import generar_reportes
from map.common.master_common import list_masters, dar_estudiantes_proyecto_grado
from map.common.pensum_common import dar_pensum_set, crear_pensum
from map.common.student_common import dar_estudiantes_de_maestria, crear_student
import json

@csrf_exempt
@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def master(request, master_id=None):

    # if not request.user.is_authenticated():
    #     return HttpResponse(unicode('Usuario sin autenticacion'), status=500)
    # else:
        if (request.method == 'GET'):
            if (master_id == None):
                data = request.GET
                if validate_data(data, attrs=['operation', 'master_name']):
                    if data['operation'] == "5":
                        try:
                            maestria = Master.objects.get(name=data['master_name'])
                            if maestria != None:
                                json_response = json.dumps(maestria.to_dict())
                                print(json_response)
                                return HttpResponse(json_response, status=200, content_type='application/json')
                            else:
                                error = error_json(2, "No existe la maestría")
                                return HttpResponse(error, status=500, content_type='application/json')
                        except Exception as e:
                            error = error_json(2, "No existe la maestría")
                            return HttpResponse(error, status=500, content_type='application/json')
                    else:
                        error = error_json(2, "No existe la maestría")
                        return HttpResponse(error, status=500, content_type='application/json')
                else:
                    response = list_masters()
                    json_response = json.dumps(response)
                    return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                data = request.GET
                if validate_data(data, attrs=['operation', 'master_name']):
                    if "operation" in data:
                        if data['operation'] == "1":
                            obj_pensumes_lista = dar_pensum_set(master_id)
                            json_response = json.dumps(obj_pensumes_lista)
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        if data['operation'] == "2":
                            obj_estudiantes_lista = dar_estudiantes_de_maestria(master_id)
                            json_response = json.dumps(obj_estudiantes_lista)
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        if data['operation'] == "3":
                            obj_estudiantes_lista = dar_estudiantes_proyecto_grado(master_id)
                            json_response = json.dumps(obj_estudiantes_lista)
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        if data['operation'] == "4":
                            generar_reportes()
                            json_response = json.dumps({"mensaje": "Reportes generados correctamente"})
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        else:
                            error = error_json(4, "No existe la operación")
                            return HttpResponse(error, status=500, content_type='application/json')

                    else:
                        master = Master.objects.get(id=master_id)
                        json_response = json.dumps(master.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.DATA
            if validate_data(data, attrs=['operation', 'name']):
                if 'operation' in data:
                    if master_id==None:
                        error = error_json(4,"Se debe agregar el id de la maestría")
                        return HttpResponse(error, status=500,content_type='application/json')

                else:
                    master = Master.objects.create(name=data['name'])
                    json_response = json.dumps(master.to_dict())
                    return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)

        elif request.method == 'PUT':
            data = request.DATA
            if master_id != None:
                if validate_data(data, attrs=['name', 'active', 'operation','code_studen', 'email_studen', 'lastname_studen', 'name_studen']):
                    if 'operation' in data:
                        if data['operation'] == "1":
                            name = data['name']
                            active = data['active']
                            obj_pensum = crear_pensum(name=name, active=active, master=master_id)
                            json_response = json.dumps(obj_pensum.to_dict())
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        elif data['operation'] == "2":
                            code_studen= data['code_studen']
                            email_studen = data['email_studen']
                            lastname_studen = data['lastname_studen']
                            name_studen = data['name_studen']
                            student_obj = crear_student(code_studen,email_studen,lastname_studen,name_studen,master_id)
                            json_response = json.dumps(student_obj.to_dict())
                            return HttpResponse(json_response, status=200, content_type='application/json')
                    else:
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