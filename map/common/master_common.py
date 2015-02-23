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
        return {master}
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
        return {master:""}
        #master == "MISO":