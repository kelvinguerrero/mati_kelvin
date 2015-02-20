from map.models import Master


def list_masters():
    lista_masters = Master.objects.all()
    lista = list()

    for obj_course in lista_masters:
        lista.append(obj_course.to_dict())

    return lista