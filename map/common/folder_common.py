from map.models import Student


def list_courses_scheme(student_code):
    lista_courses = list()
    student = Student.objects.get(code=student_code)
    if student.scheme.courses.all().count() > 0:
        lista_courses = student.scheme.courses.all()
        lista = list()
        for obj_course in lista_courses:
            lista.append(obj_course.to_dict_view())
        return lista
    return list()


#Metodo que calcula la cantidad de creditos aprobados por el estudiante
def calculate_credits(student_code):

    student = Student.objects.get(code=student_code)
    subject_list = student.subject_set.all()
    tot_credits = 0
    if subject_list.all().count() > 0:
        lista_ap = list()
        for obj_subject in subject_list:
            if obj_subject.student_status and obj_subject.grade > 3:
                lista_ap.append(obj_subject)

        for sub in lista_ap:
            print sub
            tot_credits += sub.section.course.credits

    return tot_credits


#Metodo enterga los cursos aprobados por el estudiante
def list_subject_approved(student_code):
    student = Student.objects.get(code=student_code)
    subject_list = student.subject_set.all()
    if subject_list.all().count() > 0:
        lista_ap = list()
        for obj_subject in subject_list:
            if obj_subject.student_status and obj_subject.grade > 3:
                lista_ap.append(obj_subject)
    return lista_ap

#Metodo enterga los cursos aprobados por el estudiante
def list_subject_approved_master(student_code):
    student = Student.objects.get(code=student_code)
    subject_list = student.subject_set.all()
    if subject_list.all().count() > 0:
        lista_ap = list()
        for obj_subject in subject_list:
            if obj_subject.student_status and obj_subject.grade > 3:
                lista_ap.append(obj_subject)
    return lista_ap