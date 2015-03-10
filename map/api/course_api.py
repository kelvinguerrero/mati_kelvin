from map.models import Course, Pensum
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.course_common import list_courses, dar_secciones
from map.common.section_common import crear_seccion
import json

@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def course(request, course_id=None):

    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'), status=500)
    else:
        if request.method == 'GET':
            if course_id == None:
                response = list_courses()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                data = request.GET
                if validate_data(data, attrs=['operation', 'code_curso']):
                    if "operation" in data:
                        if data['operation'] == "1":
                            if course_id == None:
                                return HttpResponse(unicode('Se debe agregar el id de la maestria'), status=500)
                            else:
                                obj_secciones = dar_secciones(course_id)
                                json_response = json.dumps(obj_secciones)
                                return HttpResponse(json_response, status=200, content_type='application/json')
                    else:
                        course = Course.objects.get(id=course_id)
                        json_response = json.dumps(course.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST
            if validate_data(data, attrs=['operation', 'code', 'name', 'credits', 'summer', 'pensum', 'crn_section',
                                          'name_section', 'semester', 'year', 'code_teacher', 'MESI', 'MBIT', 'MISO',
                                          'MATI', 'MISIS', 'pregrado', 'otros']):
                lista_attrs = list()
                lista_attrs.append('code')
                lista_attrs.append('name')
                lista_attrs.append('credits')
                lista_attrs.append('summer')
                lista_attrs.append('pensum')

                if validate_data(data, attrs=lista_attrs):
                    pensum_obj = Pensum.objects.get(id=data['pensum'])

                    course = Course.objects.create(code=data['code'],
                                                   name=data['name'],
                                                   credits=data['credits'],
                                                   summer=data['summer'],
                                                   pensum=pensum_obj)
                    json_response = json.dumps(course.to_dict())
                    return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)
        elif request.method == 'PUT':
            data = request.DATA
            if course_id != None:
                if validate_data(data, attrs=['operation', 'code', 'name', 'credits', 'summer', 'pensum', 'crn_section',
                                          'name_section', 'semester', 'year', 'code_teacher', 'MESI', 'MBIT', 'MISO',
                                          'MATI', 'MISIS', 'pregrado', 'otros']):
                    if 'operation' in data:
                        if data['operation'] == "1":
                            lista_capacity = {}
                            if 'MESI'in data:
                                lista_capacity['MESI'] = data['MESI']
                            if 'MBIT' in data:
                                lista_capacity['MBIT'] = data['MBIT']
                            if 'MISO' in data:
                                lista_capacity['MISO'] = data['MISO']
                            if 'MATI'in data:
                                lista_capacity['MATI'] = data['MATI']
                            if 'MISIS' in data:
                                lista_capacity['MISIS'] = data['MISIS']
                            if 'pregrado'in data:
                                lista_capacity['pregrado'] = data['pregrado']
                            if 'otros' in data:
                                lista_capacity['otros'] = data['otros']

                            obj_section = crear_seccion(course_id, data['crn_section'], data['name_section'], data['semester'], data['year'],
                                      data['code_teacher'], lista_capacity)

                            json_response = json.dumps(obj_section.to_dict())
                            return HttpResponse(json_response, status=200, content_type='application/json')
                    else:

                        course = Course.objects.get(id=course_id)

                        if 'code' in data:
                            course.code = data['code']
                        if 'name' in data:
                            course.name = data['name']
                        if 'credits' in data:
                            course.credits = data['credits']
                        if 'summer' in data:
                            course.summer = data['summer']
                        if 'pensum' in data:
                            pensum_obj = Pensum.objects.get(id=data['pensum'])
                            course.teacher = pensum_obj

                        course.save()
                        json_response = json.dumps(course.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)
        elif request.method == 'DELETE':
            if course_id != None:
                course_obj = Course.objects.get(id=course_id)
                if not course_obj == None:
                    course_obj.delete()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        return HttpResponse(status=400)