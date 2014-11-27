from map.models import Student


def list_students():
    lista_student = Student.objects.all()
    lista = list()

    for obj_student in lista_student:
        lista.append(obj_student.to_dict())

    return lista