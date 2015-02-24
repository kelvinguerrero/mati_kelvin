from map.models import Master
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from map.common.master_common import list_masters
from map.common.pensum_common import dar_pensum_set, crear_pensum
from map.common.student_common import dar_estudiantes_de_maestria, crear_student
import json


@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def master(request, master_id=None):

    if not request.user.is_authenticated():
        return HttpResponse(unicode('Usuario sin autenticacion'), status=500)
    else:
        if (request.method == 'GET'):
            if (master_id == None):
                response = list_masters()
                json_response = json.dumps(response)

                return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                master = Master.objects.get(id=master_id)
                json_response = json.dumps(master.to_dict())
                return HttpResponse(json_response, status=200, content_type='application/json')
        elif request.method == 'POST':
            data = request.POST
            if validate_data(data, attrs=['operation', 'name']):
                if data['operation'] == "1":
                    if master_id==None:
                        return HttpResponse(unicode('Se debe agregar el id de la maestria'), status=500)
                    obj_pensumes_lista = dar_pensum_set(master_id)
                    json_response = json.dumps(obj_pensumes_lista)
                    return HttpResponse(json_response, status=200, content_type='application/json')
                if data['operation'] == "2":
                    if master_id==None:
                        return HttpResponse(unicode('Se debe agregar el id de la maestria'), status=500)
                    obj_estudiantes_lista = dar_estudiantes_de_maestria(master_id)
                    json_response = json.dumps(obj_estudiantes_lista)
                    return HttpResponse(json_response, status=200, content_type='application/json')
                else:
                    master = Master.objects.create(name=data['name'])
                    json_response = json.dumps(master.to_dict())
                    return HttpResponse(json_response, status=200, content_type='application/json')
            else:
                return HttpResponse(status=500)

        elif request.method == 'PUT':
            data = request.DATA
            if master_id != None:
                if validate_data(data, attrs=['name', 'active', 'operation','code_studen', 'email_studen', 'lastname_studen', 'name_studen']):
                    if data['operation'] == "1":
                        name = data['name']
                        active = data['active']
                        obj_pensum = crear_pensum(name=name, active=active, master=master_id)
                        json_response = json.dumps(obj_pensum.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    elif data['operation'] == "2":
                        code_studen= data['code_studen']
                        email_studen = data['email_studen']
                        lastname_studen = data['lastname_studen']
                        name_studen = data['name_studen']
                        student_obj = crear_student(code_studen,email_studen,lastname_studen,name_studen,master_id)
                        json_response = json.dumps(student_obj.to_dict())
                        return HttpResponse(json_response, status=200, content_type='application/json')
                    else:
                        master = Master.objects.get(id=master_id)
                        if 'name' in data:
                            master.name = data['name']
                        master.save()
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