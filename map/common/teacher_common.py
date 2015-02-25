from map.models import Teacher


def list_teachers():
    lista_teacher = Teacher.objects.all()
    lista = list()

    for obj_teacher in lista_teacher:
        lista.append(obj_teacher.to_dict())

    return lista

def dar_profesor_by_code(code_profesor):
    return Teacher.objects.get(code = code_profesor)