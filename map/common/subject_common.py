__author__ = 'kelvin Guerrero'
from map.models import Subject


def list_subjects():
    lista_subject = Subject.objects.all()
    lista = list()

    for obj_subject in lista_subject:
        lista.append(obj_subject.to_dict())

    return lista