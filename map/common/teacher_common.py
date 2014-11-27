from map.models import Teacher


def list_teachers():
    lista_teacher = Teacher.objects.all()
    lista = list()

    for obj_teacher in lista_teacher:
        lista.append(obj_teacher.to_dict())

    return lista