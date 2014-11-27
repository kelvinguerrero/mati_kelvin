from map.models import Pensum


def list_pensums():
    lista_pensum = Pensum.objects.all()
    lista = list()

    for obj_pensum in lista_pensum:
        lista.append(obj_pensum.to_dict())

    return lista