__author__ = 'kelvin Guerrero'
# coding=utf-8
import os
import json


# Metodo encargado de cargar la base de datos con la información inicial
def cargar_datos():
    cargar_estudiantes_graduados()
    #cargar_estudiantes_201220()
    #cargar_estudiantes_201210()
    #cargar_estudiantes()
    #cargar_profesores()


def cargar_estudiantes_201510():

    #Parametros para la llamada de la creación de un estudiante
    BASE_PATH = 'http://localhost:8000/map/api/student/'
    headers = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Parametros para la llamada de la llamada de un estudiante
    BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
    headers_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    delimiter = '	'
    with open('cargue/estudiantes_matric_Matriculados201510.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", row['CARNET'])

            #Se llama al servicio de llamada de estudiante para verificar si este existe
            rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
            s_code = rta_buscar_estudiante.status_code

            if s_code == 500:
                json_rta = json.loads(rta_buscar_estudiante.text)['mensaje']
                if json_rta == 'No existe el estudiante':
                    data = {
                        'lastname': row['APELLIDOS'],
                        'code': row['CARNET'],
                        'email': row['EMAIL'],
                        'name': row['NOMBRES'],
                        'student_status': 1,
                        'master_id': 3
                    }
                    rta = fork_service.llamada_post(BASE_PATH, headers, data)
                    print rta.text
                else:
                    print "Error en el estudiante" + row['CARNET']

            else:
                print "Estudiante ya existe: " + row['CARNET']


def cargar_estudiantes_201220():

    #Parametros para la llamada de la creación de un estudiante
    BASE_PATH = 'http://localhost:8000/map/api/student/'
    headers = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Parametros para la llamada de un estudiante
    BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
    headers_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    delimiter = '	'
    with open('cargue/estudiantes_matric_Matriculados201220.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", row['CARNET'])

            #Se llama al servicio de llamada de estudiante para verificar si este existe
            rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
            s_code = rta_buscar_estudiante.status_code

            if s_code == 500:
                json_rta = json.loads(rta_buscar_estudiante.text)['mensaje']
                if json_rta == 'No existe el estudiante':
                    data = {
                        'lastname': row['APELLIDOS'],
                        'code': row['CARNET'],
                        'email': row['EMAIL'],
                        'name': row['NOMBRES'],
                        'student_status': 1,
                        'master_id': 3
                    }
                    rta = fork_service.llamada_post(BASE_PATH, headers, data)
                    print rta.text
                else:
                    print "Error con el estudiante:"+ row['CARNET']

            else:
                print "Estudiante ya existe: " + row['CARNET']


def cargar_estudiantes_graduados():

    #Parametros para la llamada de la creación de un estudiante
    BASE_PATH = 'http://localhost:8000/map/api/student/'
    headers = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Parametros para la llamada de un estudiante
    BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
    headers_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Parametros para actualizar los datos de un estudiante
    BASE_PATH_EDIT_STUDENT = "http://localhost:8000/map/api/student/codigo_student"
    headers_edit_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    delimiter = '	'
    with open('cargue/estudiantes_graduados.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", row['CARNET'])
            rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
            s_code = rta_buscar_estudiante.status_code
            if s_code == 500:
                json_rta = json.loads(rta_buscar_estudiante.text)['mensaje']
                if json_rta == 'No existe el estudiante':
                    data = {
                        'lastname': row['APELLIDOS'],
                        'name': row['NOMBRES'],
                        'code': row['CARNET'],
                        'student_status': 3,
                        'master_id': 3
                    }
                    rta = fork_service.llamada_post(BASE_PATH, headers, data)
                    print rta.text
                else:
                    print "Error en el estudiante" + row['CARNET']

            else:
                json_id_estudiante = json.loads(rta_buscar_estudiante.text)['id']
                print str(json_id_estudiante)+ ": estudiante"
                BASE_PATH_EDIT_STUDENT = BASE_PATH_EDIT_STUDENT.replace("codigo_student", str(json_id_estudiante))

                data_edit = {
                    'student_status': 1
                }
                rta = fork_service.llamada_post(BASE_PATH_EDIT_STUDENT, headers_edit_student, data_edit)
                print "Estudiante ya existe: " + row['CARNET']
                print "Se actualiza el estado a graduado"
                print(rta)


def cargar_estudiantes():
    file_estudiantes_path = "cargue/estudiantes.xlsx"
    xls_estudiantes = xlrd.open_workbook(file_estudiantes_path)
    hoja = xls_estudiantes.sheet_by_index(0)
    print(hoja.nrows)
    print(hoja.ncols)
    print(hoja.cell_value(0,0))
    print("llego")


def cargar_profesores():
    file_estudiantes_path = "cargue/estudiantes.xlsx"
    xls_estudiantes = xlrd.open_workbook(file_estudiantes_path)
    hoja = xls_estudiantes.sheet_by_index(0)

    BASE_PATH = 'http://localhost:8000/map/api/teacher/'
    headers = {'API_KEY': '123', 'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'}
    #print(hoja.ncols)
    #print(hoja.cell_value(0,0))
    #print("llego")
    #print(hoja.nrows)
    for row in range(hoja.nrows):
        for col in range(hoja.ncols):
            print(hoja.cell_value(row,col))
    #data = {"lastname": "", "code": "", "email": "", "name": ""}
    #fork_service.llamada_post(BASE_PATH, data, headers)

# Start execution here!
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mati.settings")
    import xlrd
    import csv
    from mati import fork_service
    cargar_datos()