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


def dar_curso_by_code(code_curso):
    obj_curso = Course.objects.get(code=code_curso)
    return obj_curso


def dar_curso_by_id(id_curso):
    obj_curso = Course.objects.get(id=id_curso)
    return obj_curso


def crear_curso(code, summer, name, credits, pensum):
    obj_course = Course.objects.get_or_create(code=code,
                                              credits=credits,
                                              name=name,
                                              summer=summer,
                                              pensum=pensum)[0]
    return obj_course


def dar_secciones(id_curso):
    obj_curso = dar_curso_by_id(id_curso)
    lista_secciones = obj_curso.section_set.all()
    lista = list()
    for obj_seccion in lista_secciones:
        lista.append(obj_seccion.to_dict_api())
    return lista

