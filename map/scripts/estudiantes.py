# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'
import csv
import json
from mati import fork_service


def run(*args):
    print args
    if 'estudiantes' in args:
        cargar_estudiantes()
    elif 'graduados' in args:
        cargar_estudiantes_graduados()
    elif 'estudiantes_201510' in args:
        cargar_estudiantes_graduados()
    elif 'estudiantes_201220' in args:
        cargar_estudiantes_graduados()


def cargar_estudiantes():
    cargar_estudiantes_201510()
    cargar_estudiantes_201220()
    cargar_estudiantes_graduados()


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
    BASE_PATH = 'http://localhost:8000/map/api/teacher/'
    headers = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Parametros para la llamada de un estudiante
    BASE_PATH_PROFESOR = "http://localhost:8000/map/api/teacher/codigo_profesor?operation=1"
    headers_profesor = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Parametros para actualizar los datos de un estudiante
    BASE_PATH_EDIT_PROFESOR = "http://localhost:8000/map/api/teacher/codigo_profesor"
    headers_edit_profesor = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    delimiter = '	'
    with open('cargue/estudiantes_graduados.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            BASE_PATH_PROFESOR = BASE_PATH_PROFESOR.replace("codigo_profesor", row['CARNET'])
            rta_buscar_profesor = fork_service.llamada_get(BASE_PATH_PROFESOR, headers_profesor)
            s_code = rta_buscar_profesor.status_code
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
                BASE_PATH_EDIT_PROFESOR = BASE_PATH_EDIT_PROFESOR.replace("codigo_student", str(json_id_estudiante))

                data_edit = {
                    'student_status': 1
                }
                rta = fork_service.llamada_post(BASE_PATH_EDIT_PROFESOR, headers_edit_profesor, data_edit)
                print "Estudiante ya existe: " + row['CARNET']
                print "Se actualiza el estado a graduado"
                print(rta)


def cargar_estudiantes_graduados():

    #Parametros para la llamada de la creación de un profesor
    BASE_PATH = 'http://localhost:8000/map/api/student/'
    headers = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Parametros para la llamada de un profesor
    BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
    headers_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }


    delimiter = '	'
    with open('cargue/estudiantes_graduados.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
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

