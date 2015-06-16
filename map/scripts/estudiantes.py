# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'
import csv
import json
from mati import fork_service
from map.scripts import maestrias


#Metodo encargado en la creación de un estudiante
def crear_estudiante( pdata ):
    #Parametros para la llamada de la creación de un estudiante
    BASE_PATH = 'http://localhost:8000/map/api/student/'
    headers = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    rta = fork_service.llamada_post(BASE_PATH, headers, pdata)
    s_code_creacion = rta.status_code

    if s_code_creacion == 500:
        json_rta = json.loads(rta.text)
        return json_rta['mensaje']
    elif s_code_creacion == 200:
        json_rta = json.loads(rta.text)
        return json_rta


def crear_estudiantes(pprograma, pcodigo , papellido, pnombre, pemail, pstatus):
     #Parametros para la llamada de la llamada de un estudiante
    BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
    headers_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", pcodigo)

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
    s_code = rta_buscar_estudiante.status_code

    if s_code == 500:
        json_rta = json.loads(rta_buscar_estudiante.text)['mensaje']
        if json_rta == 'No existe el estudiante':

            rta_dar_maestria = maestrias.dar_maestria(pprograma)
            s_code_dar_maestria = rta_dar_maestria.status_code

            if rta_dar_maestria != None:
                if s_code_dar_maestria == 500:
                    print 'No se encontro la maestría: ' + pprograma

                    rta_crear = maestrias.crear_maesria(pprograma)

                    if rta_crear == 500:
                        print "Error en la creacion de la maestria" + pprograma
                    elif rta_crear == 200:
                        print('Se creó la maestria:')
                        print rta_crear.text
                        print

                elif s_code_dar_maestria == 200:
                    decode_dar_maestria = rta_dar_maestria.text
                    json_maestria = json.loads(decode_dar_maestria)
                    master_id=json_maestria["id"]
                    data = {
                        'lastname': papellido,
                        'code': pcodigo,
                        'email': pemail,
                        'name': pnombre,
                        'student_status': pstatus,
                        'master_id': master_id
                    }
                    rta = crear_estudiante( data )
                    print("creo el estudiante:")
                    print rta
                else:
                    print "Error en el estudiante" + pcodigo
            else:
                print "Error en la busqueda de la maestría: " + pcodigo

    else:
        print "Estudiante ya existe: " + pcodigo


def cargar_estudiantes_201510():
    print "carge de estudiantes del año 201510"

    #Parametros para la llamada de la llamada de un estudiante
    # BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
    # headers_student = {
    #     'API-KEY': '123',
    #     'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    # }

    delimiter = '	'
    with open('cargue/estudiantes_matric_Matriculados201510_2.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            crear_estudiantes(row['PROGRAMA'], row['CARNET'] , row['APELLIDOS'], row['NOMBRES'], row['EMAIL'], 1)
            # BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", row['CARNET'])
            #
            # #Se llama al servicio de llamada de estudiante para verificar si este existe
            # rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
            # s_code = rta_buscar_estudiante.status_code
            #
            # if s_code == 500:
            #     json_rta = json.loads(rta_buscar_estudiante.text)['mensaje']
            #     if json_rta == 'No existe el estudiante':
            #
            #         rta_dar_maestria = maestrias.dar_maestria(row['PROGRAMA'])
            #         s_code_dar_maestria = rta_dar_maestria.status_code
            #
            #         if rta_dar_maestria != None:
            #             if s_code_dar_maestria == 500:
            #                 print 'No se encontro la maestría: ' + row['PROGRAMA']
            #
            #                 rta_crear = maestrias.crear_maesria(row['PROGRAMA'])
            #
            #                 if rta_crear == 500:
            #                     print "Error en la creacion de la maestria" + row['PROGRAMA']
            #                 elif rta_crear == 200:
            #                     print('Se creó la maestria:')
            #                     print rta_crear.text
            #                     print
            #
            #             elif s_code_dar_maestria == 200:
            #                 decode_dar_maestria = rta_dar_maestria.text
            #                 json_maestria = json.loads(decode_dar_maestria)
            #                 master_id=json_maestria["id"]
            #                 data = {
            #                     'lastname': row['APELLIDOS'],
            #                     'code': row['CARNET'],
            #                     'email': row['EMAIL'],
            #                     'name': row['NOMBRES'],
            #                     'student_status': 1,
            #                     'master_id': master_id
            #                 }
            #                 rta = crear_estudiante( data )
            #                 print("creo el estudiante:")
            #                 print rta
            #             else:
            #                 print "Error en el estudiante" + row['CARNET']
            #         else:
            #             print "Error en la busqueda de la maestría: " + row['PROGRAMA']
            #
            # else:
            #     print "Estudiante ya existe: " + row['CARNET']


def cargar_estudiantes_201220():
    print "carge de estudiantes del año 201220"

    #  #Parametros para la llamada de la llamada de un estudiante
    # BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
    # headers_student = {
    #     'API-KEY': '123',
    #     'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    # }

    delimiter = '	'

    with open('cargue/estudiantes_matric_Matriculados201220.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            crear_estudiantes(row['PROGRAMA'], row['CARNET'] , row['APELLIDOS'], row['NOMBRES'], row['EMAIL'], 1)
            # BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", row['CARNET'])
            #
            # #Se llama al servicio de llamada de estudiante para verificar si este existe
            # rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
            # s_code = rta_buscar_estudiante.status_code
            #
            # if s_code == 500:
            #     json_rta = json.loads(rta_buscar_estudiante.text)['mensaje']
            #     if json_rta == 'No existe el estudiante':
            #
            #         rta_dar_maestria = maestrias.dar_maestria(row['PROGRAMA'])
            #         s_code_dar_maestria = rta_dar_maestria.status_code
            #
            #         if rta_dar_maestria != None:
            #             if s_code_dar_maestria == 500:
            #                 print 'No se encontro la maestría: ' + row['PROGRAMA']
            #
            #                 rta_crear = maestrias.crear_maesria(row['PROGRAMA'])
            #
            #                 if rta_crear == 500:
            #                     print "Error en la creacion de la maestria" + row['PROGRAMA']
            #                 elif rta_crear == 200:
            #                     print('Se creó la maestria:')
            #                     print rta_crear.text
            #                     print
            #
            #             elif s_code_dar_maestria == 200:
            #                 decode_dar_maestria = rta_dar_maestria.text
            #                 json_maestria = json.loads(decode_dar_maestria)
            #                 master_id=json_maestria["id"]
            #                 data = {
            #                     'lastname': row['APELLIDOS'],
            #                     'code': row['CARNET'],
            #                     'email': row['EMAIL'],
            #                     'name': row['NOMBRES'],
            #                     'student_status': 1,
            #                     'master_id': master_id
            #                 }
            #                 rta = crear_estudiante( data )
            #                 print("creo el estudiante:")
            #                 print rta
            #             else:
            #                 print "Error en el estudiante" + row['CARNET']
            #         else:
            #             print "Error en la busqueda de la maestría: " + row['PROGRAMA']
            #
            # else:
            #     print "Estudiante ya existe: " + row['CARNET']


def cargar_estudiantes_graduados():

    #Parametros para la llamada de un estudiante
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
            BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
            pprograma = row["PROGRAMA"]
            papellido = row['APELLIDOS']
            pcodigo = row['CARNET']
            pnombre = row['NOMBRES']
            pstatus = 3
            print
            print(pcodigo)
            print
            BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", row['CARNET'])
            rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
            s_code = rta_buscar_estudiante.status_code
            print(rta_buscar_estudiante.text)

            if s_code == 500:

                rta_dar_maestria = maestrias.dar_maestria(pprograma)
                s_code_dar_maestria = rta_dar_maestria.status_code

                if rta_dar_maestria != None:
                    if s_code_dar_maestria == 500:
                        print 'No se encontro la maestría: ' + pprograma

                        rta_crear = maestrias.crear_maesria(pprograma)

                        if rta_crear == 500:
                            print "Error en la creacion de la maestria" + pprograma
                        elif rta_crear == 200:
                            print('Se creó la maestria:')
                            print rta_crear.text
                            print

                    elif s_code_dar_maestria == 200:
                        decode_dar_maestria = rta_dar_maestria.text
                        json_maestria = json.loads(decode_dar_maestria)
                        master_id=json_maestria["id"]
                        data = {
                            'lastname': papellido,
                            'code': pcodigo,
                            'name': pnombre,
                            'student_status': pstatus,
                            'master_id': master_id
                        }
                        rta = crear_estudiante( data )
                        print("creo el estudiante:")
                        print rta
                    else:
                        print "Error en el estudiante" + pcodigo
                else:
                    print "Error en la busqueda de la maestría: " + pcodigo

            else:
                json_id_estudiante = json.loads(rta_buscar_estudiante.text)['id']
                print str(json_id_estudiante)+": estudiante"
                BASE_PATH_EDIT_STUDENT = BASE_PATH_EDIT_STUDENT.replace("codigo_student", str(json_id_estudiante))

                data_edit = {
                    'student_status': 3
                }
                rta = fork_service.llamada_post(BASE_PATH_EDIT_STUDENT, headers_edit_student, data_edit)
                print "Estudiante ya existe: " + pcodigo
                print "Se actualiza el estado a graduado"
                print(rta)


def cargar_estudiantes( ):
    cargar_estudiantes_201510( )
    cargar_estudiantes_201220( )
    cargar_estudiantes_graduados( )


def run(*args):
    print args
    if 'estudiantes' in args:
        cargar_estudiantes( )
    elif 'graduados' in args:
        cargar_estudiantes_graduados( )
    elif 'estudiantes_201510' in args:
        cargar_estudiantes_201510( )
    elif 'estudiantes_201220' in args:
        cargar_estudiantes_201220( )
    else:
        print "comando incorrecto"