# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'

from django.views.decorators.csrf import csrf_exempt
from map.models import Subject
from map.models import Section
from map.models import Student
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.subject_common import list_subjects
import json

@csrf_exempt
@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def subject(request, subject_id=None):
    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'),status=500)
    else:
        if (request.method == 'GET'):
            if (subject_id == None):
                response = list_subjects()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                subject = Subject.objects.get(id=subject_id)
                json_response = json.dumps(subject.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST

            lista_attrs = list()
            lista_attrs.append('grade')
            lista_attrs.append('student_status')
            lista_attrs.append('student')
            lista_attrs.append('section')


            if validate_data(data, attrs=lista_attrs):

                student_obj = Student.objects.get(id=data['student'])
                section_obj = Section.objects.get(id=data['section'])
                #agregar la validacion del objeto
                subject = Subject.objects.create(grade=data['grade'],
                                                 student_status=data['student_status'],
                                                 student=student_obj,
                                                 section=section_obj
                                                 )
                json_response = json.dumps(subject.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)
        elif request.method == 'PUT':
            data = request.DATA
            if subject_id != None:
                subject = Subject.objects.get(id=subject_id)
                if 'grade' in data:
                    subject.grade = data['grade']
                if 'student_status' in data:
                    subject.student_status = data['student_status'] is 'True'
                if 'student' in data:
                    student_obj = Student.objects.get(id=data['student'])
                    subject.student = student_obj
                if 'section' in data:
                    section_obj = Section.objects.get(id=data['section'])
                    subject.section = section_obj

                #agregar la validacion de datos
                subject.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        elif request.method == 'DELETE':
            if subject_id != None:
                subject_obj = Subject.objects.get(id=subject_id)
                if not subject_obj == None:
                    subject_obj.delete()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        return HttpResponse(status=400)