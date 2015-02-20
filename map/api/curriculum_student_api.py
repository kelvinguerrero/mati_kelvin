from map.models import Student, Course
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from django.db.models.query import EmptyQuerySet
from map.common.master_common import list_masters
import json


@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def curriculum_student(request, curriculum_student_id=None):
    print "emtro" + curriculum_student_id
    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'), status=500)
    else:
        if (request.method == 'GET'):
            if curriculum_student_id==None:
                return HttpResponse(unicode('Se debe agregar el id del estudiante'), status=500)
            else:
                student = Student.objects.get(id=curriculum_student_id)
                if student.course_set.count() == 0:
                    return HttpResponse(json.dumps({}), status=200, content_type='application/json')
                else:
                    json_response = json.dumps(student.to_dict_curriculum())
                    return HttpResponse(json_response, status=200, content_type='application/json')

        elif request.method == 'POST':
            data = request.POST
            if validate_data(data, attrs=['name']):
                master = Master.objects.create(name=data['name'])

                json_response = json.dumps(master.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)

        elif request.method == 'PUT':
            data = request.DATA
            if curriculum_student_id != None:
                student = Student.objects.get(id=curriculum_student_id)

                if 'course_id' in data:
                    course_obj = Course.objects.get(id=data['course_id'])
                    student.courses.add(course_obj)

                student.save()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)

        elif request.method == 'DELETE':
            if master_id != None:
                master = Master.objects.get(id=master_id)
                if not master == None:
                    master.delete()
                return HttpResponse(status=204)
            else:
                return HttpResponse(status=500)
        return HttpResponse(status=400)