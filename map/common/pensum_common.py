from map.models import Pensum, Master
from map.common.course_common import crear_curso
from map.common.master_common import dar_maestria


def crear_pensum(name, active, master):
    obj_maestria = dar_maestria(id_master=master)
    return Pensum.objects.get_or_create(name=name, active=active, master=obj_maestria)[0]


def dar_pensum(id_pensum):
    obj_pensum = Pensum.objects.get(id=id_pensum)
    return obj_pensum


def list_pensums():
    lista_pensum = Pensum.objects.all()
    lista = list()
    for obj_pensum in lista_pensum:
        lista.append(obj_pensum.to_dict())
    return lista


def dar_cursos_pensum(id_pensum):
    obj_pensum = Pensum.objects.get(id=id_pensum)
    lista_cursos = obj_pensum.course_set.all()
    lista = list()
    for obj_curso in lista_cursos:
        lista.append(obj_curso.to_dict())
    return lista


def dar_pensum_set(id_maestria):
    obj_maestria = Master.objects.get(id=id_maestria)
    lista = list()
    for obj_pensum in obj_maestria.pensum_set.all():
        lista.append(obj_pensum.to_dict())
    return lista


def agregar_curso(id_pensum, code, summer, name, credits, pensum):
    obj_pensum = Pensum.objects.get(id=id_pensum)
    obj_curso = crear_curso(code=code, summer=summer, name=name, credits=credits, pensum=obj_pensum)
    if obj_curso!= None and obj_pensum != None:
        return obj_curso
    return False

