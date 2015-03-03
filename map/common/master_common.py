from map.models import Master


def list_masters():
    lista_masters = Master.objects.all()
    lista = list()

    for obj_course in lista_masters:
        lista.append(obj_course.to_dict())

    return lista


def crear_maestria(name):
    obj_master = Master.objects.get_or_create(name=name)[0]
    return obj_master


def dar_maestria(id_master):
    try:
        obj_master = Master.objects.get(id=id_master)
        return obj_master
    except Master.DoesNotExist:
        return None