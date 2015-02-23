from map.models import Master, Student
from map.common.folder_common import list_subject_approved_master
from map.common.student_common import dar_maestria


def list_masters():
    lista_masters = Master.objects.all()
    lista = list()

    for obj_course in lista_masters:
        lista.append(obj_course.to_dict())

    return lista


def structure_master_courses(code_student):
    master = dar_maestria(code_student)
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
                               "totMATI": totMATI
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
                               "comp": comp
                               }}
        return datos
    else:
        #si es profundizacion
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
            datos = {"datos": {"inte": inte,
                               "comp": comp,
                               "prof": prof,
                               "totMiso": totMiso,
                               "comp": comp,
                               "fundMISO": fundMISO,
                                "fundMISIS": fundMISIS,
                                "fundMBIT": fundMBIT
                               }}
        return datos