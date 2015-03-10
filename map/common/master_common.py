from map.models import Master
from map.common.student_common import   tiene_proyecto_grado, ingles_aprobado, dar_cantidad_creditos, \
                                        dar_cursos_maestria, dar_cursos_otra_maestria


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


def dar_maestria_nombre(name_master):
    try:
        obj_master = Master.objects.get(name=name_master)
        return obj_master
    except Master.DoesNotExist:
        return None


def dar_estudiantes_proyecto_grado(id_master):
    master = dar_maestria(id_master)
    estudiantes = master.student_set.all()
    json_general =[]
    for obj_student in estudiantes:
        if tiene_proyecto_grado(obj_student.id):
            json_student = []
            nota = ingles_aprobado(id_student=obj_student.id)
            if nota == False or nota == None:
                json_student.append("Ingles no aprobado")
            else:
                json_student.append({"Ingles": nota.to_dict()})
            tot_creditos = dar_cantidad_creditos(id_student=obj_student.id)
            json_student.append({"creditos_aprobados":tot_creditos})
            cursos_maestr = dar_cursos_maestria(student_id=obj_student.id)
            json_student.append({"cursos_mati": cursos_maestr})
            cursos_maestr_otra = dar_cursos_otra_maestria(student_id=obj_student.id)
            json_student.append({"cursos_otra_maestria": cursos_maestr_otra})
            json_student.append({"estudiante": obj_student.to_dict()})
            json_general.append(json_student)
    return json_general