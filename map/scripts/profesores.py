# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'
import csv
import json
from mati import fork_service


def run(*args):
    print args
    if 'profesores' in args:
        cargar_profesor()


def cargar_profesor():
    print "carge de profesores"

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

    delimiter = '	'
    with open('cargue/estudiantes_graduados.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            BASE_PATH_PROFESOR = BASE_PATH_PROFESOR.replace("codigo_profesor", row['CARNET'])
            rta_buscar_profesor = fork_service.llamada_get(BASE_PATH_PROFESOR, headers_profesor)
            s_code = rta_buscar_profesor.status_code
            if s_code == 500:
                json_rta = json.loads(rta_buscar_profesor.text)['mensaje']
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
                print "Profesor ya existe: " + row['CARNET']
