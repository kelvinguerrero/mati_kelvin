__author__ = 'kelvin Guerrero'
from map.models import Section, Capacity, Subject
from map.common.teacher_common import dar_profesor_by_code
from map.common.course_common import dar_curso_by_id
from map.common.student_common import dar_estudiante_codigo


def dar_seccion(id_seccion):
    try:
        obj_section = Section.objects.get(id=id_seccion)
        return obj_section
    except Section.DoesNotExist:
        return None


def dar_seccion_crn(crn_seccion):
    try:
        obj_section = Section.objects.get(crn=crn_seccion)
        return obj_section
    except Section.DoesNotExist:
        return None


def list_sections():
    lista_sections = Section.objects.all()
    lista = list()
    for obj_section in lista_sections:
        lista.append(obj_section.to_dict())
    return lista


def list_sections_api():
    lista_sections = Section.objects.all()
    lista = list()
    for obj_section in lista_sections:
        lista.append(obj_section.to_dict())
    return lista


def crear_seccion(course_id, crn_section, name_section, semester, year, code_teacher,
                  lista_capacity):
    obj_profesor = dar_profesor_by_code(code_teacher)
    ob_course = dar_curso_by_id(id_curso=course_id)
    obj_section = Section.objects.get_or_create(crn=crn_section,
                                                name=name_section,
                                                semester=semester,
                                                year=year,
                                                teacher=obj_profesor,
                                                course=ob_course)[0]
    for capacidad in lista_capacity:
        Capacity.objects.create(name=capacidad, capacity=lista_capacity[capacidad], section=obj_section)
    return obj_section


def dar_capacidad(id_seccion):
    obj_seccion = dar_seccion(id_seccion)
    capacidad = obj_seccion.capacity_set.all()
    lista = list()
    for obj_cap in capacidad:
        lista.append(obj_cap.to_dict())
    return lista


def dar_notas_seccion(id_seccion):
    obj_seccion = dar_seccion(id_seccion=id_seccion)
    notas = obj_seccion.subject_set.all()
    lista = list()
    for nota in notas:
        lista.append(nota.to_dict())
    return lista


def agergar_nota(code_student, id_section, grade):
    obj_student = dar_estudiante_codigo(code_student=code_student)
    obj_section = dar_seccion(id_seccion=id_section)
    if obj_student!=None and obj_section != None:
        student_status = False
        if grade >= 3:
            student_status = True
        obj_subject = Subject.objects.create(grade=grade,
                                             section=obj_section,
                                             student=obj_student,
                                             student_status=student_status)
        return obj_subject
    else:
        return None


def cambiar_estado(id_section, estado):
    obj_section = dar_seccion(id_seccion=id_section)
    if obj_section != None:
        obj_section.status = estado
        return obj_section
    else:
        return None