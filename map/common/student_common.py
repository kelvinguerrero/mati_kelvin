__author__ = 'kelvin Guerrero'
from map.models import Student, Scheme
from map.common.master_common import dar_maestria
from map.common.course_common import dar_curso_by_code


def dar_estudiante(id_student):
    obj_student = Student.objects.get(id=id_student)
    return obj_student

def list_students():
    lista_student = Student.objects.all()
    lista = list()
    for obj_student in lista_student:
        lista.append(obj_student.to_dict())
    return lista


def dar_maestria_de_estudiante(code_student):
    student = Student.objects.get(code=code_student)
    return student.master.name


def dar_estudiantes_de_maestria(master_id):
    obj_master = dar_maestria(id_master=master_id)
    studen_set = obj_master.student_set.all()
    lista = list()
    for obj_student in studen_set:
        lista.append(obj_student.to_dict())
    return lista


#Metodo encargado de crear un estudiante
# params: code => codigo del estudiante, email => email del estudiante, lastname => apellido del estudiante,
#         name => Nombre del estudiante, master
def crear_student(code, email, lastname, name, master):
    obj_mas = dar_maestria(master)
    p = Student.objects.get_or_create(code=code, email=email, lastname=lastname, name=name, master=obj_mas)[0]
    return p


def dar_notas(id_student):
    obj_student = dar_estudiante(id_student=id_student)
    notas = obj_student.subject_set.all()
    lista = list()
    for nota in notas:
        lista.append(nota.to_dict())
    return lista


def dar_crear_scheme(name):
    obj_scheme = Scheme.objects.get_or_create(name=name, active=True)[0]
    return obj_scheme


def crear_plan_studios(id_student, nombre, curso1, curso2, curso3,
                       curso4, curso5, curso6, curso7, curso8, curso9, curso10):
    obj_student = dar_estudiante(id_student=id_student)
    obj_scheme = obj_student.scheme

    if obj_student.scheme == None:
        obj_scheme = dar_crear_scheme(nombre)
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