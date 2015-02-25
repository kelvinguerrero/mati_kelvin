__author__ = 'kelvin Guerrero'
from map.models import Student, Master
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.student_common import list_students, dar_notas, crear_plan_studios

import json


@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def student(request, student_id=None):
    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'),status=500)
    else:
        if (request.method == 'GET'):
            if student_id is None:
                response = list_students()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                student = Student.objects.get(id=student_id)
                json_response = json.dumps(student.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST
            if validate_data(data, attrs=['operation', 'master_id', 'code',
                                          'email', 'lastname', 'name', 'student_status',
                                          'total_approved_credits', 'total_credits_actual_semester',
                                          'nombre','curso1','curso2','curso3','curso4','curso5','curso6',
                                          'curso7','curso8','curso9','curso10']):
                if "operation" in data:
                    if data['operation'] == "1":
                        notas = dar_notas(id_student=student_id)
                        json_response = json.dumps(notas)
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    if data['operation'] == "2":
                        plan = crear_plan_studios(student_id, data['nombre'], data['curso1'], data['curso2'], data['curso3'],
                                                  data['curso4'], data['curso5'], data['curso6'], data['curso7'], data['curso8'],
                                                  data['curso9'], data['curso10'])
                        json_response = json.dumps(plan.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
                else:

                    lista_attrs = list()
                    lista_attrs.append('master_id')
                    lista_attrs.append('code')
                    lista_attrs.append('email')
                    lista_attrs.append('lastname')
                    lista_attrs.append('name')
                    lista_attrs.append('student_status')
                    lista_attrs.append('total_approved_credits')
                    lista_attrs.append('total_credits_actual_semester')

                    if validate_data(data, attrs=lista_attrs):
                        master_obj = Master.objects.get(id=data['master_id'])

                        #agregar la validacion del objeto
                        student = Student.objects.create(code=data['code'],
                                                         email=data['email'],
                                                         lastname=data['lastname'],
                                                         name=data['name'],
                                                         student_status=data['student_status'],
                                                         total_approved_credits=data['total_approved_credits'],
                                                         total_credits_actual_semester=data['total_credits_actual_semester'],
                                                         master=master_obj
                                                         )
                        json_response = json.dumps(student.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    else:
                        return HttpResponse(status=500)
        elif request.method == 'PUT':
            data = request.DATA
            if student_id is not None:
                student = Student.objects.get(id=student_id)

                if 'code' in data:
                    student.code = data['code']
                if 'email' in data:
                    student.email = data['email']
                if 'lastname' in data:
                    student.lastname = data['lastname']
                if 'name' in data:
                    student.name = data['name']
                if 'student_status' in data:
                    student.student_status = data['student_status']
                if 'total_approved_credits' in data:
                    student.total_approved_credits = data['total_approved_credits']
                if 'total_credits_actual_semester' in data:
                    student.total_credits_actual_semester = data['total_credits_actual_semester']
                #agregar la validacion de datos
                student.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        elif request.method == 'DELETE':
            if student_id is not None:
                student_obj = Student.objects.get(id=student_id)
                if student_obj is not None:
                    student_obj.delete()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        return HttpResponse(status=400)