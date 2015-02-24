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


def dar_curso(code_curso):
    obj_curso = Course.objects.get(code=code_curso)
    return obj_curso


def crear_curso(code, summer, name, credits, pensum):
    obj_course = Course.objects.get_or_create(code=code,
                                              credits=credits,
                                              name=name,
                                              summer=summer,
                                              pensum=pensum)[0]
    return obj_course