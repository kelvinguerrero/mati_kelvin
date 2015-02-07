from map.models import Course, Pensum
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.course_common import list_courses
import json

@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def course(request, course_id=None):

    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'),status=500)
    else:
        if (request.method == 'GET'):
            if (course_id == None):
                response = list_courses()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                course = Course.objects.get(id=course_id)
                json_response = json.dumps(course.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST

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
                course = Course.objects.get(id=course_id)
                print 'Valida:' + str(course.clean())

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
                return HttpResponse(status=204)
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