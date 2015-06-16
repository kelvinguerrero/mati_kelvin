# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'

from django.views.decorators.csrf import csrf_exempt
from map.models import Student, Master
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.student_common import   list_students, dar_notas, crear_plan_studios, \
                                        dar_scheme, ingles_aprobado, tiene_cruso, \
                                        total_cursos_maestria_elect, tiene_proyecto_grado
from map.common.error_common import error_json
import json

@csrf_exempt
@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def student(request, student_id=None):

    # if not request.user.is_authenticated():
    #     return HttpResponse(unicode('Usuario sin autenticacion'), status=500)
    # else:
        if request.method == 'GET':
            if student_id is None:
                response = list_students()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                data = request.GET
                if validate_data(data, attrs=['operation', 'code_curso']):
                    if "operation" in data:
                        if data['operation'] == "1":
                            notas = dar_notas(id_student=student_id)
                            json_response = json.dumps(notas)
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        if data['operation'] == "6":
                            try:
                                student = Student.objects.get(code=student_id)
                                if student != None:
                                    json_response = json.dumps(student.to_dict())
                                    return HttpResponse(json_response, status=200, content_type='application/json')
                                else:
                                    error = error_json(2, "No existe el estudiante")
                                    return HttpResponse(error, status=500, content_type='application/json')
                            except Exception as e:
                                error = error_json(2, "No existe el estudiante")
                                return HttpResponse(error, status=500, content_type='application/json')
                        if data['operation'] == "3":
                            plan = dar_scheme(student_id)
                            if plan != None:
                                json_response = json.dumps(plan.to_dict())
                                return HttpResponse(json_response, status=200, content_type='application/json')
                            else:
                                error = error_json(2, "No existe plan de estudios")
                                return HttpResponse(error, status=500, content_type='application/json')
                        if data['operation'] == "4":
                            nota = ingles_aprobado(id_student=student_id)
                            if nota != None:
                                if nota == False:
                                    json_response = json.dumps({"Respuesta": "No tiene aprobado Ingles"})
                                    return HttpResponse(json_response, status=200, content_type='application/json')
                                else:
                                    json_response = json.dumps(nota.to_dict())
                                    return HttpResponse(json_response, status=200, content_type='application/json')
                            else:
                                error = error_json(2, "No existe el estudiante")
                                return HttpResponse(error, status=500, content_type='application/json')
                        if data['operation'] == "5":
                            nota = tiene_cruso(id_student=student_id, code_curso_temp=data['code_curso'])
                            if nota != None:
                                if nota == False:
                                    json_response = json.dumps({"Respuesta": "No tiene el curso " + data['code_curso'] + " aprobado"})
                                    return HttpResponse(json_response, status=200, content_type='application/json')
                                else:
                                    json_response = json.dumps(nota.to_dict())
                                    return HttpResponse(json_response, status=200, content_type='application/json')
                            else:
                                error = error_json(2, "No existe el estudiante")
                                return HttpResponse(error, status=500, content_type='application/json')
                        if data['operation'] == "7":
                            cursos = total_cursos_maestria_elect(student_id)
                            son_response = json.dumps(cursos)
                            return HttpResponse(son_response, status=200, content_type='application/json')
                        if data['operation'] == "8":
                            cursos = tiene_proyecto_grado(student_id)
                            if cursos == False:
                                rta = {"Respuesta": "No tiene proyecto de grado"}
                                return HttpResponse(json.dumps(rta), status=500, content_type='application/json')
                            else:
                                son_response = json.dumps(cursos)
                                return HttpResponse(son_response, status=200, content_type='application/json')

                else:
                    try:
                        student = Student.objects.get(id=student_id)
                        if student != None:
                            json_response = json.dumps(student.to_dict())
                            return HttpResponse(json_response, status=200, content_type='application/json')
                    except Exception as e:
                            error = error_json(3, "No se existe el estudiante: " + str(e))
                            return HttpResponse(error, status=500, content_type='application/json')
                    else:
                        error = error_json(2, "No existe el estudiante")
                        return HttpResponse(error, status=500, content_type='application/json')
        elif request.method == 'POST':
            data = request.DATA
            if validate_data(data, attrs=['operation', 'master_id', 'code', 'email', 'lastname', 'name', 'student_status',
                                          'nombre', 'curso1', 'curso2', 'curso3', 'curso4', 'curso5', 'curso6',
                                          'curso7', 'curso8', 'curso9', 'curso10', 'code_curso']):
                if "operation" in data:
                    if student_id == None:
                        error = error_json(4, "Se debe agregar el id del estudiante")
                        return HttpResponse(error, status=500, content_type='application/json')

                    else:

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

                    if validate_data(data, attrs=lista_attrs):


                        #agregar la validacion del objeto
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
                            if 'student_status' in data:
                                parametros.update({'student_status': data['student_status']})
                            if 'master_id' in data:
                                parametros.update({'master': Master.objects.get(id=data['master_id'])})
                                #master_obj = Master.objects.get(id=data['master_id'])
                            student = Student.objects.create(**parametros)
                            # student = Student.objects.create(code=data['code'],
                            #                                  email=data['email'],
                            #                                  lastname=data['lastname'],
                            #                                  name=data['name'],
                            #                                  student_status=data['student_status'],
                            #                                  master=master_obj
                            #                                  )
                            json_response = json.dumps(student.to_dict())
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        except Exception as e:
                            error = error_json(3, "No se creo el estudiante " + str(e))
                            return HttpResponse(error, status=500, content_type='application/json')

                    else:
                        error = error_json(3, "No se creo el estudiante")
                        return HttpResponse(error, status=500, content_type='application/json')
        elif request.method == 'PUT':
            data = request.DATA
            if student_id is not None:
                vstudent = Student.objects.get(id=student_id)

                if 'code' in data:
                    vstudent.code = data['code']
                if 'email' in data:
                    vstudent.email = data['email']
                if 'lastname' in data:
                    vstudent.lastname = data['lastname']
                if 'name' in data:
                    vstudent.name = data['name']
                if 'student_status' in data:
                    vstudent.student_status = data['student_status']
                #if 'total_approved_credits' in data:
                #    student.total_approved_credits = data['total_approved_credits']
                #if 'total_credits_actual_semester' in data:
                #    student.total_credits_actual_semester = data['total_credits_actual_semester']
                #agregar la validacion de datos
                vstudent.save()
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