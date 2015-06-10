# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'

from django.views.decorators.csrf import csrf_exempt
from map.models import Section, Course, Teacher
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.section_common import list_sections, dar_capacidad, dar_notas_seccion,  agergar_nota, cambiar_estado
from map.common.error_common import error_json
import json

@csrf_exempt
@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def section(request, section_id=None):
    # if not request.user.is_authenticated():
    #     return HttpResponse(unicode('Usuario sin autenticacion'),status=500)
    # else:
        if (request.method == 'GET'):
            if (section_id == None):
                response = list_sections()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                data = request.GET
                if validate_data(data, attrs=['operation']):
                    if "operation" in data:
                        if data['operation'] == "1":
                            if section_id!=None:
                                capacidad = dar_capacidad(id_seccion=section_id)
                                json_response = json.dumps(capacidad)
                                return HttpResponse(json_response, status=200, content_type='application/json')
                        if data['operation'] == "2":
                            if section_id!=None:
                                notas = dar_notas_seccion(id_seccion=section_id)
                                json_response = json.dumps(notas)
                                return HttpResponse(json_response, status=200, content_type='application/json')
                        else:
                            error = error_json(1, "No existe la operació")
                            return HttpResponse(error, status=200, content_type='application/json')
                    else:
                        section = Section.objects.get(id=section_id)
                        json_response = json.dumps(section.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST
            if validate_data(data, attrs=['operation', 'crn', 'name', 'semester',
                                          'year', 'teacher', 'course', 'code_student',
                                          'grade', 'status']):
                if "operation" in data:
                    if section_id==None:
                        error = error_json(3, "Se debe agregar el id de la sección")
                        return HttpResponse(error, status=500,content_type='application/json')
                    else:
                        if data['operation'] == "4":
                                if section_id!=None:
                                    notas = cambiar_estado(id_section=section_id, estado=data['status'])
                                    if notas == None:
                                        error = error_json(5, "Verificar datos")
                                        return HttpResponse(error, status=200, content_type='application/json')
                                    json_response = json.dumps(notas.to_dict())
                                    return HttpResponse(json_response, status=200, content_type='application/json')
                        if data['operation'] == "3":
                            notas = agergar_nota(code_student=data['code_student'], id_section=section_id,
                                                 grade=data['grade'])
                            if notas == None:
                                error = error_json(5, "Verificar datos")
                                return HttpResponse(error, status=200, content_type='application/json')
                            json_response = json.dumps(notas.to_dict())
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        else:
                            error = error_json(1, "No existe la operació")
                            return HttpResponse(error, status=200, content_type='application/json')

                else:
                    lista_attrs = list()
                    lista_attrs.append('crn')
                    lista_attrs.append('name')
                    lista_attrs.append('semester')
                    lista_attrs.append('year')
                    lista_attrs.append('teacher')
                    lista_attrs.append('course')
                    lista_attrs.append('status')

                    if validate_data(data, attrs=lista_attrs):
                        teacher_obj = Teacher.objects.get(id=data['teacher'])
                        course_obj = Course.objects.get(id=data['course'])
                        print"hola"
                        section = Section.objects.create(crn=data['crn'],
                                                         name=data['name'],
                                                         semester=data['semester'],
                                                         year=data['year'],
                                                         status=data['status'],
                                                         teacher=teacher_obj,
                                                         course=course_obj)
                        json_response = json.dumps(section.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    else:
                        return HttpResponse(status=500)
            else:
                return HttpResponse(status=500)
        elif request.method == 'PUT':
            data = request.DATA
            if section_id != None:
                section = Section.objects.get(id=section_id)

                if 'crn' in data:
                    section.crn = data['crn']
                if 'name' in data:
                    section.name = data['name']
                if 'semester' in data:
                    section.semester = data['semester']
                if 'year' in data:
                    section.year = data['year']
                if 'teacher' in data:
                    teacher_obj = Teacher.objects.get(id=data['teacher'])
                    section.teacher = teacher_obj
                if 'course' in data:
                    course_obj = Course.objects.get(id=data['course'])
                    section.course = course_obj

                section.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        elif request.method == 'DELETE':
            if section_id is not None:
                section_obj = Section.objects.get(id=section_id)
                if not section_obj is None:
                    section_obj.delete()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        return HttpResponse(status=400)