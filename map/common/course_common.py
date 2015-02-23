from map.models import Course


def list_courses():
    lista_courses = Course.objects.all()
    lista = list()

    for obj_course in lista_courses:
        lista.append(obj_course.to_dict_view())
    return lista


def list_courses_api():
    lista_courses = Course.objects.all()
    lista = list()

    for obj_course in lista_courses:
        lista.append(obj_course.to_dict_api())

    return lista