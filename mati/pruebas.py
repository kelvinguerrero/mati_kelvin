__author__ = 'kelvin Guerrero'
# coding=utf-8
import os
import requests
import json


#Creacion de escenarios
def pruebas():
    print "llamada de pruebas"
    print "llamada de token"
    llamada_token()
    print "llamada de get contar creditos"
    llamada_get_req_contar_creditos_aprobados()
    print "llamada de post"
    id = llamada_post_course()
    print "llamada de put"
    llamada_put_course(id)
    print "llamada de delete"
    llamada_delete_course(id)


def llamada_token():
    BASE_PATH = 'http://localhost:8000/api-token-auth/'
    s = requests.Session()
    headers = {'API_KEY': '123'}
    s.verify = False
    datos = {'username': 'pepa', 'password': 'pepa'}
    r = requests.post(BASE_PATH, headers=headers, data=datos)
    print r
    print r.text


def llamada_get_req_contar_creditos_aprobados():
    BASE_PATH = 'http://localhost:8000/map/api/folder/199024632/?operation=1'
    s = requests.Session()
    s.verify = False
    headers = {'API_KEY': '123', 'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'}
    r = requests.get(BASE_PATH, headers=headers)
    print r
    print(r.text)


def llamada_post_course():
    BASE_PATH = 'http://localhost:8000/map/api/course/'
    data = {"code": "c_nuevo4", "name": "nombreCurso",
            "credits": "2", "summer": "True", "pensum": "4"}
    headers = {'API_KEY': '123', 'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'}
    s = requests.Session()
    s.verify = False
    r = requests.post(BASE_PATH, headers=headers,data=data)
    print r
    print(r.text)
    data = json.loads(r.text)
    return data["id"]


def llamada_put_course(id):
    BASE_PATH = 'http://localhost:8000/map/api/course/'+str(id)+'/'
    data = {"code": "c_nuevo4", "name": "nombreCurso2",
            "credits": "2", "summer": "True", "pensum": "2"}
    headers = {'API_KEY': '123', 'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'}
    s = requests.Session()
    s.verify = False
    r = requests.put(BASE_PATH, headers=headers, data=data)
    print r
    print(r.text)


def llamada_delete_course(id):
    BASE_PATH = 'http://localhost:8000/map/api/course/'+str(id)+'/'
    headers = {'API_KEY': '123', 'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'}
    s = requests.Session()
    s.verify = False
    r = requests.delete(BASE_PATH, headers=headers)
    print r
    print(r.text)



# Start execution here!
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mati.mati.settings')
    pruebas()