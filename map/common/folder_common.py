# coding=utf-8
from map.models import Student
from map.common.student_common import dar_maestria_de_estudiante, dar_estudiante_codigo,dar_scheme


def list_courses_scheme(student_code):
    stu = dar_estudiante_codigo(student_code)
    plan = dar_scheme(stu.id)
    return plan


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
            tot_credits += sub.section.course.credits

    return tot_credits


#Metodo enterga los cursos aprobados por el estudiante
def list_subject_approved(student_code):
    student = Student.objects.get(code=student_code)
    subject_list = student.subject_set.all()
    lista_ap = list()
    if subject_list.all().count() > 0:
        for obj_subject in subject_list:
            if obj_subject.student_status and obj_subject.grade > 3:
                lista_ap.append(obj_subject.to_dict())
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


def structure_master_courses(code_student):
    master = dar_maestria_de_estudiante(code_student)
    if master != None:
        if master == "MATI":
            prof = 7
            elect = 2
            inte = 1
            totMATI = False
            datos={}
            list_subject = list_subject_approved_master(code_student)
            for object in list_subject:
                if object.section.course.pensum.master.name == master:
                    if object.section.course == "Proyecto final":
                        inte = inte - 1
                    else:
                        if prof > 0:
                            prof = prof - 1
                    if prof == 0:
                        totMATI = True
                else:
                    if elect>0:
                        elect = elect -1
            datos = {"datos": {"prof": prof,
                                   "elect": elect,
                                   "prof": prof,
                                   "inte": inte,
                                   "totMATI": totMATI,
                                  "master":master
                                   }}
            return datos

        elif master == "MBIT":
            return {master}
        elif master == "MESI":
            return {master}
        elif master == "MISIS":
            prof = 3
            compMisis = 2
            totMisis = False
            comp = 2
            inte = 3
            datos={}
            list_subject = list_subject_approved_master(code_student)
            for object in list_subject:
                if object.section.course.pensum.master.name == master:
                    if object.section.course == "Tesis I":
                        inte = inte - 1
                    elif object.section.course == "Tesis II":
                        inte = inte - 2
                    else:
                        if prof > 0:
                            prof = prof - 1
                        elif compMisis > 0:
                            compMisis = compMisis -1
                    if prof == 0 and compMisis == 0:
                        totMisis = True
                else:
                    if comp > 0:
                        comp = comp - 1
                datos = {"datos": {"tesis": inte,
                                   "totMisis": totMisis,
                                   "prof": prof,
                                   "compMisis": compMisis,
                                   "comp": comp,
                                   "master":master
                                   }}
            return datos
        else:
            #si es profundizacion MISO
            fundMISO=1
            fundMISIS=1
            fundMBIT=1
            totMiso=False
            prof=4
            comp=2
            inte=1
            datos={}
            list_subject = list_subject_approved_master(code_student)
            for object in list_subject:
                if object.section.course.pensum.master.name == master:
                    if object.section.course == "Proyecto Integrador":
                        inte = inte - 1
                    else:
                        if prof > 0:
                            prof = prof - 1
                        elif fundMISO > 0:
                            fundMISO = fundMISO -1
                    if prof == 0 and fundMISO == 0:
                        totMiso = True
                else:
                    if fundMISIS + fundMBIT > 0:
                        if object.section.course.pensum.master.name == "MISIS" and fundMISIS > 0:
                            fundMISIS = fundMISIS - 1
                        elif object.section.course.pensum.master.name == "MBIT" and fundMBIT > 0:
                            fundMBIT = fundMBIT - 1
                        elif comp > 0:
                            comp = comp - 1
                datos = {"datos": {"proyectoIntegrador": inte,
                                   "complemento": comp,
                                   "profundización": prof,
                                   "CursosMisoCompletos": totMiso,
                                   "complemento": comp,
                                   "fundamentaciónMISO": fundMISO,
                                    "fundamentaciónMISIS": fundMISIS,
                                    "fundamentaciónMBIT": fundMBIT,
                                    "maestría": master
                                   }}
            return datos
    else:
        return None