# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'
import csv
import json
from mati import fork_service


def crear_profesor(p_apellido, p_nombre, p_code, p_email):

    #Parametros para la creación de una Maestria
    BASE_PATH_TEACHER_CREATE = "http://localhost:8000/map/api/teacher/"
    headers_course_create = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }
    data = {
            'lastname': p_apellido,
            'code': p_code,
            'email': p_email,
            'name': p_nombre
           }
    rta = fork_service.llamada_post(BASE_PATH_TEACHER_CREATE, headers_course_create, data)
    return rta


def dar_profesor( p_code ):
    #Parametros para la llamada de la llamada de una maestría
    BASE_PATH_TEACHER = "http://localhost:8000/map/api/teacher/code_teacher?operation=1"
    headers_course = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    BASE_PATH_TEACHER = BASE_PATH_TEACHER.replace("code_teacher", p_code)

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_teacher = fork_service.llamada_get(BASE_PATH_TEACHER, headers_course)
    return rta_buscar_teacher


def run(*args):
    print args
    if 'profesores' in args:
        cargar_profesores("profesores_201510.csv")


def cargar_profesores(p_ruta_archivo):
    print "carge de profesores"

    delimiter = '	'
    with open('cargue/'+p_ruta_archivo, 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            p_codigo = row['MATERIA']+ "-" + row['CURSO']
            p_nombre = row['NOMBRE_CURSO']
            p_creditos = 4
            p_vacacional = False
#            if row['MATERIA'] == "ARTI":

 #               p_pensum =

            validar_cargue_curso(p_codigo, p_nombre, p_creditos, p_vacacional, p_pensum)

            rta_profesor = dar_profesor( row['ID_PROFESOR'] )
            s_code = rta_profesor.status_code
            if s_code == 500:
                json_rta = json.loads(rta_profesor.text)['mensaje']
                if  'No existe el profesor' in json_rta and row['ID_PROFESOR'] in json_rta:
                    nombre= row['PROFESOR'].split(",")[1]
                    apellido= row['PROFESOR'].split(",")[0]
                    email= None
                    rta_crear = crear_profesor(apellido, nombre, row["ID_PROFESOR"], email)

                    print rta_crear.text
                else:
                    print "Error en el profesor" + row['ID_PROFESOR']

            else:
                print "Profesor ya existe: " + row['ID_PROFESOR']

#def validar_cargue_curso(p_codigo, p_nombre, p_creditos, p_vacacional, p_pensum):
