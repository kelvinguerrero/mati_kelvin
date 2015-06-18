    # BASE_PATH = 'http://localhost:8000/map/api/course/'
    # data = {"code": "c_nuevo4", "name": "nombreCurso",
    #         "apellido": "2", "email": "True", "pensum": "4"}
    # headers = {'API_KEY': '123', 'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'}
__author__ = 'kelvin Guerrero'
# coding=utf-8
import os
import requests
import json


def llamada_post(pbase_path, pheaders, pdata):
    s = requests.Session()
    s.verify = False
    jsondata = json.dumps(pdata)
    r = requests.post(pbase_path, headers=pheaders, data=jsondata)
    return r


def llamada_get(pbase_path, pheaders):
    s = requests.Session()
    s.verify = False
    r = requests.get(pbase_path, headers=pheaders)
    return r


def llamada_put(pbase_path, pheaders, pdata):
    s = requests.Session()
    s.verify = False
    r = requests.put(pbase_path, headers=pheaders, data=pdata)
    return r