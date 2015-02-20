# coding=utf-8
import os

def populate():

    #Carga de Mestrias
    mati = ["MATI", "MBC", "MBIT", "MESI", "MISIS", "MISO"]

    print "carga de maestrias"
    for maestria in mati:
        print maestria
        add_master(name=maestria)

    #Cursos de MATI
    print "carga de cursos de MATI"
    cursosMati = {
                    "ARTI-4101": {"name": "Gerencia de Proyectos para Arquitectos", "credits": 4, "summer": False},
                    "ARTI-4102": {"name": "Comunicación Efectiva para Arquitectos", "credits": 4, "summer": False},
                    "ARTI-4104": {"name": "Fundamentos para Arquitectos", "credits": 4, "summer": False},
                    "ARTI-4202": {"name": "Arquitectura de Información", "credits": 4, "summer": False},
                    "ARTI-4203": {"name": "Arquitectura de Infraestructura de TI", "credits": 4, "summer": False},
                    "ARTI-4204": {"name": "Arquitectura de Seguridad", "credits": 4, "summer": False},
                    "ARTI-4201": {"name": "Arquitectura de Solución", "credits": 4, "summer": False},
                    "ARTI-4205": {"name": "Arquitectura de Procesos de Negocio", "credits": 4, "summer": False},
                    "ARTI-4103": {"name": "Arquitectura de Negocios y Estrategia de TI", "credits": 4, "summer": False},
                    "ARTI-4106": {"name": "Arquitectura Empresarial", "credits": 4, "summer": False}
                }


    for a in cursosMati:
        print a
        for b in cursosMati[a]:
            print b
            print cursosMati[a][b]





    # add_page(cat=python_cat,
    #     title="How to Think like a Computer Scientist",
    #     url="http://www.greenteapress.com/thinkpython/")
    #
    # add_page(cat=python_cat,
    #     title="Learn Python in 10 Minutes",
    #     url="http://www.korokithakis.net/tutorials/python/")
    #
    # django_cat = add_cat("Django")
    #
    # add_page(cat=django_cat,
    #     title="Official Django Tutorial",
    #     url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    #
    # add_page(cat=django_cat,
    #     title="Django Rocks",
    #     url="http://www.djangorocks.com/")
    #
    # add_page(cat=django_cat,
    #     title="How to Tango with Django",
    #     url="http://www.tangowithdjango.com/")
    #
    # frame_cat = add_cat("Other Frameworks")
    #
    # add_page(cat=frame_cat,
    #     title="Bottle",
    #     url="http://bottlepy.org/docs/dev/")
    #
    # add_page(cat=frame_cat,
    #     title="Flask",
    #     url="http://flask.pocoo.org")

    # # Print out what we have added to the user.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print "- {0} - {1}".format(str(c), str(p))

def add_master(name):
    p = Master.objects.get_or_create(name=name)[0]
    return p


def add_course(pensum, code, credits, name, summer):
    p = Master.objects.get_or_create(name=name)[0]
    return p

#Metodo encargado en definir la creacion de un pensumdef add_pensum(name, active, master):
    obj_master = Master.objects.get(master)
    if obj_master != None:
        p = Pensum.objects.get_or_create(name=name, active=active)[0]
        obj_master.pensum_set = p

    return p

#
# def add_cat(name):
#     c = Category.objects.get_or_create(name=name)[0]
#     return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mati.settings')
    from map.models import Master, Pensum, Course
    populate()