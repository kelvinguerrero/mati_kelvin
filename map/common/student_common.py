from map.models import Student
from map.common.master_common import dar_maestria


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