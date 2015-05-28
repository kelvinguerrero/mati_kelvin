from map.models import Report, Master
from map.common.student_common import dar_cantidad_creditos, tiene_proyecto_grado, \
    ingles_aprobado, dar_cursos_otra_maestria, dar_cursos_maestria


def crear_json_est_pg(id_maestria):
    master = Master.objects.get(id=id_maestria)
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
            json_student.append({"cursos_otra_maestria":cursos_maestr_otra})
            json_student.append({"estudiante": obj_student.to_dict()})
            json_general.append(json_student)
    return json_general


def generar_reportes():
    maestria = Master.objects.get(name="MATI")
    json_master_estudiantes = crear_json_est_pg(maestria.id)

    try:
        reporte=Report.objects.get(name="Candidatos proyecto grado", master=maestria.id)
        reporte.json=json_master_estudiantes
        reporte.save(update_fields=["json"])

    except Report.DoesNotExist:
        print("ERROR")
        reporte = Report.objects.create(name="Candidatos proyecto grado", master=maestria.id)
        reporte.json= json_master_estudiantes


def dar_reporte_candidatos_proyecto_grado(maestriaid):
    maestria = Master.objects.get(id=maestriaid)
    reporte_estudiantes_proyecto = Report.objects.get(name="Candidatos proyecto grado", master=maestria.id)
    json_master_estudiantes = reporte_estudiantes_proyecto.json
    return json_master_estudiantes