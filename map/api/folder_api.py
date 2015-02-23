# coding=utf-8
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.folder_common import calculate_credits, list_subject_approved, list_courses_scheme
import json

@expose_service(['POST'], public=True)
def folder(request, student_code_id=None):
    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'), status=500)
    else:
        if (request.method == 'POST'):

            if student_code_id==None:
                return HttpResponse(unicode('Se debe agregar el código del estudiante'), status=500)
            else:
                data = request.POST
                if validate_data(data, attrs=['operation']):
                    if data['operation'] == "1":
                        return HttpResponse(json.dumps(calculate_credits(student_code_id)), status=200, content_type='application/json')
                    elif data['operation'] == "2":
                        json_response = json.dumps(list_subject_approved(student_code_id))
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    elif data['operation'] == "3":
                        json_response = json.dumps(list_courses_scheme(student_code_id))
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    else:
                        return HttpResponse(unicode('No se llamo una operación correcta'), status=500)
                else:
                    return HttpResponse(unicode('No se agrego una operación correcta'), status=500)