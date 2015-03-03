__author__ = 'kelvin Guerrero'
# coding=utf-8

from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.error_common import error_json
from map.common.folder_common import calculate_credits, list_subject_approved, list_courses_scheme, structure_master_courses
import json

@expose_service(['POST'], public=True)
def folder(request, student_code_id=None):
    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'), status=500)
    else:
        if (request.method == 'POST'):

            if student_code_id==None:
                error = error_json(4, "Se debe agregar el código del estudiante")
                return HttpResponse(error, status=500,content_type='application/json')
            else:
                data = request.POST
                if validate_data(data, attrs=['operation', 'student_code']):
                    if data['operation'] == "1":
                        return HttpResponse(json.dumps(calculate_credits(student_code_id)), status=200, content_type='application/json')
                    elif data['operation'] == "2":
                        json_response = json.dumps(list_subject_approved(student_code_id))
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    elif data['operation'] == "3":
                        json_response = json.dumps(list_courses_scheme(student_code_id))
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    elif data['operation'] == "4":
                        datos = structure_master_courses(student_code_id)
                        if datos != None:
                            json_response = json.dumps(datos)
                            return HttpResponse(json_response, status=200, content_type='application/json')
                        else:
                            error = error_json(4, "No existe el estudiante")
                            return HttpResponse(error, status=400, content_type='application/json')


                    else:
                        return HttpResponse(unicode('No se llamo una operación correcta'), status=500)
                else:
                    return HttpResponse(unicode('No se agrego una operación correcta'), status=500)