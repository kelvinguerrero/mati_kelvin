__author__ = 'kelvin Guerrero'
# coding=utf-8

from map.models import Section, Course, Teacher
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.section_common import list_sections, dar_capacidad, dar_notas_seccion
import json


@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def section(request, section_id=None):
    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'),status=500)
    else:
        if (request.method == 'GET'):
            if (section_id == None):
                response = list_sections()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                section = Section.objects.get(id=section_id)
                json_response = json.dumps(section.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST
            if validate_data(data, attrs=['operation', 'crn', 'name', 'semester', 'year', 'teacher', 'course']):
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
                        json_response = json.dumps({"Error":1, "mensaje": "No existe esa operación"})
                        return HttpResponse(json_response, status=500, content_type='application/json')
                else:
                    lista_attrs = list()
                    lista_attrs.append('crn')
                    lista_attrs.append('name')
                    lista_attrs.append('semester')
                    lista_attrs.append('year')
                    lista_attrs.append('teacher')
                    lista_attrs.append('course')

                    if validate_data(data, attrs=lista_attrs):
                        teacher_obj = Teacher.objects.get(id=data['teacher'])
                        course_obj = Course.objects.get(id=data['course'])

                        section = Section.objects.create(crn=data['crn'],
                                                         name=data['name'],
                                                         semester=data['semester'],
                                                         year=data['year'],
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