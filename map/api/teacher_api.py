# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'

from django.views.decorators.csrf import csrf_exempt
from map.models import Teacher
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.teacher_common import list_teachers
from map.common.error_common import error_json

import json

@csrf_exempt
@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def teacher(request, teacher_id=None):

    # if not request.user.is_authenticated():
    #     return HttpResponse(unicode('Usuario sin autenticacion'),status=500)
    # else:
        if (request.method == 'GET'):
            if (teacher_id == None):
                response = list_teachers()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                data = request.GET
                if validate_data(data, attrs=['operation']):
                    if "operation" in data:
                        if data['operation'] == "1":
                            try:
                                teacher = Teacher.objects.get(code=teacher_id)
                                if teacher != None:
                                    json_response = json.dumps(teacher.to_dict())
                                    return HttpResponse(json_response, status=200, content_type='application/json')
                                else:
                                    error = error_json(2, "No existe el profesor:" + str(teacher_id))
                                    return HttpResponse(error, status=500, content_type='application/json')
                            except Exception as e:
                                error = error_json(2, "No existe el profesor:" + str(teacher_id))
                                return HttpResponse(error, status=500, content_type='application/json')
                    else:
                        teacher = Teacher.objects.get(id=teacher_id)
                        if teacher != None:
                            json_response = json.dumps(teacher.to_dict())
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        else:
                            error = error_json(2, "No existe el profesor:" + str(teacher_id))
                            return HttpResponse(error, status=500, content_type='application/json')
        elif request.method == 'POST':
            data = request.DATA

            lista_attrs = list()
            lista_attrs.append('code')
            lista_attrs.append('email')
            lista_attrs.append('lastname')
            lista_attrs.append('name')

            if validate_data(data, attrs=lista_attrs):
                try:
                    parametros = {}
                    if 'code' in data:
                        parametros.update({'code': data['code']})
                    if 'email' in data:
                        parametros.update({'email': data['email']})
                    if 'lastname' in data:
                        parametros.update({'lastname': data['lastname']})
                    if 'name' in data:
                        parametros.update({'name': data['name']})

                    teacher = Teacher.objects.create(**parametros)
                    json_response = json.dumps(teacher.to_dict())
                    return HttpResponse(json_response, status=200, content_type='application/json')
                except Exception as e:
                    error = error_json(3, "No se creo el profesor " + str(e))
                    return HttpResponse(error, status=500, content_type='application/json')
            else:
                return HttpResponse(status=500)
        elif request.method == 'PUT':
            data = request.DATA
            if teacher_id != None:
                course = Teacher.objects.get(id=teacher_id)

                if 'code' in data:
                    course.code = data['code']
                if 'email' in data:
                    course.email = data['email']
                if 'lastname' in data:
                    course.lastname = data['lastname']
                if 'name' in data:
                    course.name = data['name']

                course.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        elif request.method == 'DELETE':
            if teacher_id != None:
                teacher_obj = Teacher.objects.get(id=teacher_id)
                if not teacher_obj == None:
                    teacher_obj.delete()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        return HttpResponse(status=400)