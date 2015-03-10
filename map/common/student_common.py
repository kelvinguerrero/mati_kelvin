__author__ = 'kelvin Guerrero'
from map.models import Student, Scheme, Scheme_courses
from map.common.course_common import dar_curso_by_code
from map.common.master_common import *


def dar_cursos_maestria(student_id):
    stude = Student.objects.get(id=student_id)
    maestria_name = stude.master.name
    cursos=list()
    if stude.scheme != None:
        lista = stude.scheme.courses.all()
        for course_temp in lista:
            if course_temp.pensum.master.name == maestria_name:
                cursos.append(course_temp.to_dict())
    return cursos


def dar_cursos_otra_maestria(student_id):
    stude = Student.objects.get(id=student_id)
    maestria_name = stude.master.name
    cursos=list()
    if stude.scheme != None:
        lista = stude.scheme.courses.all()
        for course_temp in lista:
            if course_temp.pensum.master.name != maestria_name:
                cursos.append(course_temp.to_dict())
    return cursos


def total_cursos_maestria_elect(student_id):
    stude = Student.objects.get(id=student_id)
    maestria_name = stude.master.name
    cursos = 0
    cursos_otros=0
    if stude.scheme != None:
        lista = stude.scheme.courses.all()
        for course_temp in lista:
            if course_temp.pensum.master.name == maestria_name:
                cursos = cursos+1
            cursos_otros = cursos_otros +1
    return {"cursos_otros": cursos_otros, "cursos_mestria": cursos}


def dar_cantidad_creditos(id_student):
    notas = dar_notas_obj(id_student)
    creditos = 0
    for nota in notas:
        if nota.grade >= 3:
            creditos = creditos + nota.section.course.credits
    return creditos


def tiene_proyecto_grado(id_student):
    student = dar_estudiante(id_student)
    master = dar_maestria_de_estudiante(student.code)
    esquema = dar_scheme(student.id)
    creditos = dar_cantidad_creditos(student.id)
    semes_cant_cursos = creditos/12
    if esquema != None:
        for course in esquema.courses.all():
            sc = Scheme_courses.objects.get(scheme_id=esquema.id, course_id=course.id)
            #if sc.semester >= semes_cant_cursos:
            rta = verificar_proyecto_maestria(master, course.code)
            if rta:
                return rta
        return False
    else:
        return False


def verificar_proyecto_maestria(master, code_curso):
    print(code_curso)
    if master == "MATI" and code_curso == "ARTI4301":
            return True
    if master == "MBIT" and (code_curso == "MBIT4302" or code_curso == "MBIT4301"):
            return True
    if master == "MESI" and (code_curso == "MSIN4302" or code_curso == "MSIN4301"):
            return True
    if master == "MESI" and (code_curso == "MSIN4302" or code_curso == "MSIN4301"):
            return True
    if master == "MISO" and (code_curso == "MISO4301" or code_curso == "MISO4302"):
            return True
    return False


def tiene_cruso(id_student, code_curso_temp):
    obj_student = dar_estudiante(id_student=id_student)
    if obj_student != None:
        for sub in obj_student.subject_set.all():
            code_curso = sub.section.course.code
            if code_curso == code_curso_temp:
                return sub
        return False
    else:
        return None


def ingles_aprobado(id_student):
    obj_student = dar_estudiante(id_student=id_student)
    if obj_student != None:
        for sub in obj_student.subject_set.all():
            code_curso = sub.section.course.code
            if code_curso == "LENG0001":
                return sub
        return False
    else:
        return None

# def buscar_curso_por_codigo(code_course,id_student):
#
#     obj_student = dar_estudiante(id_student)
#     if obj_student != None:
#         obj_student.section
#     return None


def dar_estudiante(id_student):
    try:
        obj_student = Student.objects.get(id=id_student)
        return obj_student
    except Student.DoesNotExist:
        return None


def dar_estudiante_codigo(code_student):
    try:
        obj_student = Student.objects.get(code=code_student)
        return obj_student
    except Student.DoesNotExist:
        return None


def list_students():
    lista_student = Student.objects.all()
    lista = list()
    for obj_student in lista_student:
        lista.append(obj_student.to_dict())
    return lista


def dar_maestria_de_estudiante(code_student):
    try:
        student = Student.objects.get(code=code_student)
        return student.master.name
    except Student.DoesNotExist:
        return None


def dar_estudiantes_de_maestria(master_id):
    try:
        obj_master = Master.objects.get(id=master_id)

    except Master.DoesNotExist:
        return None

    studen_set = obj_master.student_set.all()
    lista = list()
    for obj_student in studen_set:
        lista.append(obj_student.to_dict())
    return lista


def dar_estudiantes_de_maestria_obj(master_id):
    try:
        obj_master = Master.objects.get(id=master_id)
    except Master.DoesNotExist:
        obj_master = None
    if obj_master != None:
        studen_set = obj_master.student_set.all()
        lista = list()
        for obj_student in studen_set:
            lista.append(obj_student)
        return lista
    return None

#Metodo encargado de crear un estudiante
# params: code => codigo del estudiante, email => email del estudiante, lastname => apellido del estudiante,
#         name => Nombre del estudiante, master
def crear_student(code, email, lastname, name, master):
    obj_mas = dar_maestria(master)
    p = Student.objects.get_or_create(code=code, email=email, lastname=lastname, name=name, master=obj_mas)[0]
    return p


def verificar_existe_curso_aprobado(code_curso, code_student):
    stude = Student.objects.get(code = code_student)
    curso = dar_curso_by_code(code_curso)
    if curso != None:
        lista = dar_notas(stude.id)
        for nota in lista:
            curso_temp = nota.section.course
            if curso_temp.name == curso.name and nota.grade >3:
                return True
        return False
    return False


def dar_notas_obj(id_student):
    obj_student = dar_estudiante(id_student=id_student)
    notas = obj_student.subject_set.all()
    lista = list()
    i = 0
    for nota in notas:
        lista.append(nota)
        i= i+1
    return lista


def dar_notas(id_student):
    obj_student = dar_estudiante(id_student=id_student)
    notas = obj_student.subject_set.all()
    lista = list()
    i = 0
    for nota in notas:
        lista.append(nota.to_dict())
        i= i+1
    return lista


def dar_crear_scheme(name):
    obj_scheme = Scheme.objects.get_or_create(name=name)[0]
    return obj_scheme


def dar_scheme(id_student):
    obj_student = dar_estudiante(id_student=id_student)
    obj_scheme = obj_student.scheme
    if obj_scheme != None:
        return obj_scheme
    return None


def crear_plan_studios(id_student, nombre, curso1, curso2, curso3,
                       curso4, curso5, curso6, curso7, curso8, curso9, curso10):
    obj_student = dar_estudiante(id_student=id_student)
    if obj_student.scheme == None:
        obj_scheme = dar_crear_scheme(nombre+ "" + str(id_student))
    else:
        scheme = obj_student.scheme
        scheme.delete()
        obj_student.save()
        obj_scheme = dar_crear_scheme(nombre + "" + str(id_student))

    if curso1 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso1))

    if curso2 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso2))

    if curso3 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso3))

    if curso4 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso4))

    if curso5 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso5))

    if curso6 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso6))

    if curso7 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso7))

    if curso8 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso8))

    if curso9 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso9))

    if curso10 != None:
        obj_scheme.courses.add(dar_curso_by_code(code_curso=curso10))

    obj_student.scheme = obj_scheme
    obj_student.save()
    return obj_scheme