from map.models import Section


def list_sections():
    lista_sections = Section.objects.all()
    lista = list()

    for obj_section in lista_sections:
        lista.append(obj_section.to_dict())

    return lista

def list_sections_api():
    lista_sections = Section.objects.all()
    lista = list()

    for obj_section in lista_sections:
        lista.append(obj_section.to_dict_api())

    return lista