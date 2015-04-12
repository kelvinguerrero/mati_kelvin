from map.common.master_common import dar_estudiantes_proyecto_grado
from map.models import Report


def generar_reportes():
    json_master_estudiantes = dar_estudiantes_proyecto_grado()
    reporte_estudiantes_proyecto = Report.objects.create(name="Candidatos proyecto grado", json= json_master_estudiantes)


def dar_reporte_candidatos_proyecto_grado():
    json_master_estudiantes = Report.objects.get(name="Candidatos proyecto grado")
    return json_master_estudiantes