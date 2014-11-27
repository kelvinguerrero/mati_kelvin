from map.models import Section, Course, Teacher
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.section_common import list_sections_api
import json


@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def section(request, section_id=None):

    if (request.method == 'GET'):
        if (section_id == None):
            response = list_sections_api()
            json_response = json.dumps(response)

            return HttpResponse(json_response, status=200, content_type='application/json')
        else:
            section = Section.objects.get(id=section_id)
            json_response = json.dumps(section.to_dict_api())
            return HttpResponse(json_response, status=200, content_type='application/json')
    elif request.method == 'POST':
        data = request.POST

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
            json_response = json.dumps(section.to_dict_api())
            return HttpResponse(json_response, status=200, content_type='application/json')
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
                teacher_obj = Teacher.objects.get(id=data['teacher'])
                section.teacher = teacher_obj
            if 'teacher' in data:
                section.name = data['teacher']
            if 'course' in data:
                course_obj = Course.objects.get(id=data['course'])
                section.course = course_obj

            section.save()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=500)
    elif request.method == 'DELETE':
        if section_id != None:
            section_obj = Section.objects.get(id=section_id)
            if not section_obj == None:
                section_obj.delete()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=500)
    return HttpResponse(status=400)