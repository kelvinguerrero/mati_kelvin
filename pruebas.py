__author__ = 'kelvin Guerrero'
# coding=utf-8
import os
import random

#Creacion de escenarios
def pruebas():
    for i in range(1, 10):
        stude = Student.objects.all()
        for stu in stude:
            for sub in stu.subject_set.all():
                print sub.section.name


def dar_seccion(id_seccion):
    try:
        obj_section = Section.objects.get(id=id_seccion)
        return obj_section
    except Section.DoesNotExist:
        return None

#Metodo encargado de crear un plan de estudio del estudiante
def add_course_grade(section_crn, student_code, grade):
    sect_obj = Section.objects.get(crn=section_crn)
    stud_obj = Student.objects.get(code=student_code)
    student_status = False
    if grade >= 3:
        student_status = True
    subj_obj = Subject.objects.get_or_create(grade=grade,
                                             section=sect_obj,
                                             student=stud_obj,
                                             student_status=student_status)
    return subj_obj


#Metodo encargado de crear un plan de estudio del estudiante
def add_couse_scheme(scheme, planEstudio, code_student):
        for cursos in planEstudio[code_student]:
            curso_obj = Course.objects.get(code=planEstudio[code_student][cursos])
            scheme.courses.add(curso_obj)
            student_obj = Student.objects.get(code=code_student)
            student_obj.scheme = scheme
            student_obj.save()


#Metodo encargado de crear un plan de estudio del estudiante
def add_scheme(name):
    obj_scheme = Scheme.objects.get_or_create(name=name)[0]
    return obj_scheme


#Metodo encargado de crear o dar un profesor
# params:   code => el codigo del profesor,
#           email => email del profesor, lastname => Apellido del profesor,
#           name => Nombre del profesor
def add_teacher(code, email, lastname, name):
    obj_teacher = Teacher.objects.get_or_create(code=code, email=email, lastname=lastname, name=name)[0]
    return obj_teacher


#Metodo encargado de crear una maestria
# params: name => nombre de la maestria
def add_master(name):
    p = Master.objects.get_or_create(name=name)[0]
    return p


#Metodo encargado de crear un estudiante
# params: code => codigo del estudiante, email => email del estudiante, lastname => apellido del estudiante,
#         name => Nombre del estudiante, master
def add_student(code, email, lastname, name, master):
    p = Student.objects.get_or_create(code=code, email=email, lastname=lastname, name=name, master=master)[0]
    return p


#Metodo encargado crear un curso
def add_course(pensum, code, credits, name, summer):
    obj_course = Course.objects.get_or_create(code=code,
                                              credits=credits,
                                              name=name,
                                              summer=summer,
                                              pensum=pensum)[0]
    return obj_course


#Metodo encargado crear una sección
def add_section(crn, name, semester, year, teacher, course, capacity, status):
    obj_section = Section.objects.get_or_create(crn=crn,
                                                name=name,
                                                semester=semester,
                                                year=year,
                                                teacher=teacher,
                                                course=course,
                                                status=status)[0]
    for capacidad in capacity:
        Capacity.objects.create(name=capacidad, capacity=capacity[capacidad], section=obj_section)
    return obj_section


#Metodo encargado en definir la creacion de un pensum
def add_pensum(name, active, master):
    if master != None:
        obj_pensum = Pensum.objects.get_or_create(name="Pensum_" + name,
                                                  active=active,
                                                  master=master)[0]
    return obj_pensum


# Start execution here!
if __name__ == '__main__':
    print "Iniciando población de datos base"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mati.settings')
    from map.models import Master, Pensum, Course, Teacher, Section, Capacity, Student, Scheme,Subject
    from map.common.course_common import dar_curso_by_code
    pruebas()