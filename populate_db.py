# coding=utf-8
import os


# Metodo encargado de cargar la base de datos con la información inicial
def populate():
    #Carga de profesores
    print "carga de profesores"
    profesores = {
                    200017271: {"name": "JORGE HUMBERTO", "lastname": "ARIAS BEDOYA", "email": "jor-aria@uniandes.edu.co"},
                    198714604: {"name": "GREGORIO IVAN ERNESTO", "lastname": "BECERRA RODRIGUEZ", "email": "gie.becerra10@uniandes.edu.co"},
                    79505041: {"name": "DARIO ERNESTO", "lastname": "CORREAL", "email": "dcorreal@uniandes.edu.co"},
                    199617196: {"name": "MARIA DEL PILAR", "lastname": "VILLAMIL GIRALDO", "email": "mavillam@uniandes.edu.co"},
                    79419382: {"name": "HAROLD ENRIQUE", "lastname": "CASTRO BARRERA", "email": "hcastro@uniandes.edu.co"},
                    85462189: {"name": "YESID", "lastname": "DONOSO", "email": "ydonoso@uniandes.edu.co"},
                    79232014: {"name": "JORGE ALBERTO", "lastname": "VILLALOBOS SALCEDO", "email": "jvillalo@uniandes.edu.co"},
                    198016691: {"name": "EDUARDO", "lastname": "GONGORA MORENO", "email": "egongora@uniandes.edu.co"},
                    197810037: {"name": "RAFAEL ENRIQUE", "lastname": "GOMEZ DIAZ", "email": "ragomez@uniandes.edu.co"},
                    194814117: {"name": "FRANCISCO", "lastname": "RUEDA FAJARDO", "email": "frueda@uniandes.edu.co"},
                    199427762: {"name": "SANDRA JULIETA", "lastname": "RUEDA RODRIGUEZ", "email": "sarueda@uniandes.edu.co"},
                    000000001: {"name": "Kelly", "lastname": "Garcés Pernett", "email": "kj.garces971@uniandes.edu.co"},
                    000000002: {"name": "MIGUEL", "lastname": "NAVARRO SANINT", "email": "mi-navar@uniandes.edu.co"},
                    000000003: {"name": "Rubby", "lastname": "Casallas Gutierrez", "email": "rcasalla@uniandes.edu.co"},
                    000000004: {"name": "Juan Pablo", "lastname": "Fernandez Ramirez", "email": "jp.fernandez29@uniandes.edu.co"},
                    000000005: {"name": "Milton", "lastname": "Quiroga Becerra", "email": "mquiroga@uniandes.edu.co"},
                    000000006: {"name": "Juan Diego", "lastname": "Jiménez", "email": "jujimene@uniandes.edu.co"},
                    000000007: {"name": "RICARDO", "lastname": "GOMEZ DIAZ", "email": "ricgomez@uniandes.edu.co"},
                    800000000: {"name": "Victor", "lastname": "Toro Córdoba", "email": "vm.toro815@uniandes.edu.co"},
                    900000000: {"name": "Oscar", "lastname": "González Rojas", "email": "o-gonza1@uniandes.edu.co"},
                    110000000: {"name": "Oscar", "lastname": "Ávila Cifuentes", "email": "oj.avila@uniandes.edu.co"},
                    120000000: {"name": "Ana Lucia", "lastname": "Duque Salazar", "email": "al.duque58@uniandes.edu.co"},
                    130000000: {"name": "Jorge Arias", "lastname": "Bedoya", "email": "bedoya@uniandes.edu.co"},
                    140000000: {"name": "María Esther", "lastname": "Ordóñez", "email": "mordonez2013@uniandes.edu.co"},
                    0: {"name": "Sin asignar", "lastname": "ninguno", "email": "no-reply@uniandes.edu.co"},
                    200021872: {"name": "MARIO EDUARDO", "lastname": "SANCHEZ PUCCINI", "email": "mar-san1@uniandes.edu.co"}}

    for profesor in profesores:
        obj_profesor = add_teacher(profesor, profesores[profesor]["email"],
                                   profesores[profesor]["lastname"],
                                   profesores[profesor]["name"])
        print obj_profesor.name

    #Carga de Mestrias
    mati = ["MATI", "MBC", "MBIT", "MESI", "MISIS", "MISO"]

    print "carga de maestrias"
    for maestria in mati:
        print maestria
        obj_maestria = add_master(name=maestria)
        obj_pensum = add_pensum(name=maestria, active=True, master=obj_maestria)

#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MATI
    print "carga de cursos de MATI"

    cursosMati = {
        "ARTI4101": {"name": "Gerencia de Proyectos para Arquitectos", "credits": 4, "summer": False},
        "ARTI4102": {"name": "Comunicación Efectiva para Arquitectos", "credits": 4, "summer": False},
        "ARTI4103": {"name": "Arquitectura de Negocios y Estrategia de TI", "credits": 4, "summer": False},
        "ARTI4104": {"name": "Fundamentos para Arquitectos", "credits": 4, "summer": False},
        "ARTI4201": {"name": "Arquitectura de Solución", "credits": 4, "summer": False},
        "ARTI4202": {"name": "Arquitectura de Información", "credits": 4, "summer": False},
        "ARTI4203": {"name": "Arquitectura de Infraestructura de TI", "credits": 4, "summer": False},
        "ARTI4204": {"name": "Arquitectura de Seguridad", "credits": 4, "summer": False},
        "ARTI4205": {"name": "Arquitectura de Procesos de Negocio", "credits": 4, "summer": False},
        "ARTI4301": {"name": "Proyecto final", "credits": 4, "summer": False},
        "ARTI4106": {"name": "Arquitectura Empresarial", "credits": 4, "summer": False}}

    for codigo in cursosMati:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MATI"),
            code=codigo,
            credits=cursosMati[codigo]["credits"],
            name=cursosMati[codigo]["name"],
            summer=cursosMati[codigo]["summer"])

    print "carga de secciones de MATI"
    seccionesMati = {
        13183: {"course": "ARTI4101", "name": "1", "semester": 1, "year": 2015, "teacher": 79505041},
        13579: {"course": "MBIT4101", "name": "2", "semester": 1, "year": 2015, "teacher": 120000000},
        12663: {"course": "ARTI4103", "name": "1", "semester": 1, "year": 2015, "teacher": 79232014},
        13981: {"course": "ARTI4104", "name": "2", "semester": 1, "year": 2015, "teacher": 198714604},
        13982: {"course": "ARTI4106", "name": "1", "semester": 1, "year": 2015, "teacher": 130000000},
        12664: {"course": "ARTI4201", "name": "1", "semester": 1, "year": 2015, "teacher": 79505041},
        12667: {"course": "ARTI4202", "name": "1", "semester": 1, "year": 2015, "teacher": 140000000},
        12665: {"course": "ARTI4203", "name": "1", "semester": 1, "year": 2015, "teacher": 79419382},
        13185: {"course": "ARTI4204", "name": "1", "semester": 1, "year": 2015, "teacher": 85462189},
        13285: {"course": "MBIT4302", "name": "1", "semester": 1, "year": 2015, "teacher": 200021872},
        13582: {"course": "ARTI4301", "name": "1", "semester": 1, "year": 2015, "teacher": 79505041}}

    for seccion in seccionesMati:
        add_section(
            crn=seccion,
            name=seccionesMati[seccion]["name"],
            semester=seccionesMati[seccion]["semester"],
            year=seccionesMati[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMati[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMati[seccion]["course"])
        )
#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MBC
    print "carga de cursos de MBC"
    cursosMbc = {
        "1": {"name": "Bioinformática", "credits": 4, "summer": False},
        "2": {"name": "Algoritmos en Biología Computacional", "credits": 4, "summer": False},
        "3": {"name": "Fundamentos en programación para ciencias biológicas", "credits": 4, "summer": False},
        "4": {"name": "Biología Molecular Avanzada", "credits": 4, "summer": False},
        "5": {"name": "Biología Cuantitativa", "credits": 4, "summer": False},
        "6": {"name": "Procesamiento de datos biológicos", "credits": 4, "summer": False},
        "7": {"name": "Computación de alto desempeño para ciencias biológicas", "credits": 4, "summer": False},
        "8": {"name": "Computación visual para ciencias biológicas", "credits": 4, "summer": False},
        "9": {"name": "Modelamiento de redes", "credits": 4, "summer": False},
        "0": {"name": "Analisis de secuencias", "credits": 4, "summer": False},
        "10": {"name": "Biología de sistemas", "credits": 4, "summer": False},
        "11": {"name": "Biología sintética", "credits": 4, "summer": False},
        "12": {"name": "Introducción a la ingeniería de proteinas", "credits": 4, "summer": False},
        "13": {"name": "Modelamientos matemáticos en biología", "credits": 4, "summer": False}}

    for codigo in cursosMbc:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBC"),
            code="",
            credits=cursosMbc[codigo]["credits"],
            name=cursosMbc[codigo]["name"],
            summer=cursosMbc[codigo]["summer"])

#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MBIT
    print "carga de cursos de MBIT"
    cursosMbit = {
        "MBIT4101": {"name": "Habilidades Gerenciales en TI", "credits": 4, "summer": False},
        "MBIT4201": {"name": "Emprendimiento y Negocios Electrónicos", "credits": 4, "summer": False},
        "MBIT4202": {"name": "Gobierno de TI", "credits": 4, "summer": False},
        "MBIT4203": {"name": "Business Analytics", "credits": 4, "summer": False},
        "MBIT4204": {"name": "Gestión de Servicios de TI", "credits": 4, "summer": False},
        "MBIT4301": {"name": "PROYECTO FINAL", "credits": 4, "summer": False},
        "MBIT4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MBIT4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MBIT4205": {"name": "Fundamentos de Gerencia de TI", "credits": 4, "summer": False}}

    for codigo in cursosMbit:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBIT"),
            code=codigo,
            credits=cursosMbit[codigo]["credits"],
            name=cursosMbit[codigo]["name"],
            summer=cursosMbit[codigo]["summer"])


    #Secciones de MBIT
    print "carga de secciones de MBIT"
    seccionesMesi = {
        16852: {"course": "MBIT4101", "name": "1", "semester": 1, "year": 2015, "teacher": 800000000},
        15804: {"course": "MBIT4101", "name": "2", "semester": 1, "year": 2015, "teacher": 800000000},
        13984: {"course": "MBIT4201", "name": "1", "semester": 1, "year": 2015, "teacher": 800000000},
        16853: {"course": "MBIT4201", "name": "2", "semester": 1, "year": 2015, "teacher": 194814117},
        13985: {"course": "MBIT4202", "name": "1", "semester": 1, "year": 2015, "teacher": 900000000},
        14598: {"course": "MBIT4203", "name": "1", "semester": 1, "year": 2015, "teacher": 199617196},
        14599: {"course": "MBIT4204", "name": "1", "semester": 1, "year": 2015, "teacher": 110000000},
        14600: {"course": "MBIT4205", "name": "1", "semester": 1, "year": 2015, "teacher": 800000000},
        17118: {"course": "MBIT4301", "name": "1", "semester": 1, "year": 2015, "teacher": 0},
        17119: {"course": "MBIT4302", "name": "1", "semester": 1, "year": 2015, "teacher": 0},
        17120: {"course": "MBIT4303", "name": "1", "semester": 1, "year": 2015, "teacher": 0}}

    for seccion in seccionesMesi:
        add_section(
            crn=seccion,
            name=seccionesMesi[seccion]["name"],
            semester=seccionesMesi[seccion]["semester"],
            year=seccionesMesi[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMesi[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMesi[seccion]["course"])
        )

#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MESI
    print "carga de cursos de MESI"
    cursosMbit = {
        "MSIN4201": {"name": "Modelos de Seguridad – Aplicaciones y Análisis de Estándares", "credits": 4,"summer": False},
        "MSIN4203": {"name": "Gerencia de CSIRTs y Manejo de Incidentes", "credits": 4, "summer": False},
        "MSIN4301": {"name": "PROYECTO FINAL", "credits": 4, "summer": False},
        "MSIN4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MSIN4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MSIN4101": {"name": "Ingeniería Criptográfica y su Aplicación en TI", "credits": 4, "summer": False}}

    for codigo in cursosMbit:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBIT"),
            code=codigo,
            credits=cursosMbit[codigo]["credits"],
            name=cursosMbit[codigo]["name"],
            summer=cursosMbit[codigo]["summer"])

    #Secciones de MESI
    print "carga de secciones de MESI"
    seccionesMesi = {
        15850: {"course": "MSIN4101", "name": "1", "semester": 1, "year": 2015, "teacher": 000000005},
        14607: {"course": "MSIN4201", "name": "1", "semester": 1, "year": 2015, "teacher": 199427762},
        15851: {"course": "MSIN4203", "name": "1", "semester": 1, "year": 2015, "teacher": 000000006},
        14609: {"course": "MSIN4302", "name": "1", "semester": 1, "year": 2015, "teacher": 000000004},
        14608: {"course": "MSIN4301", "name": "1", "semester": 1, "year": 2015, "teacher": 000000007},
        16217: {"course": "MSIN4303", "name": "1", "semester": 1, "year": 2015, "teacher": 000000004}}

    for seccion in seccionesMesi:
        add_section(
            crn=seccion,
            name=seccionesMesi[seccion]["name"],
            semester=seccionesMesi[seccion]["semester"],
            year=seccionesMesi[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMesi[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMesi[seccion]["course"])
        )


#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MISIS
    print "carga de cursos de MISIS"
    cursosIsis = {
        "ISIS-4422": {"name": "Servicios móviles y redes de próxima generación", "credits": 4, "summer": False},
        "ISIS-4518": {"name": "Sistemas de Recomendación", "credits": 4, "summer": False},
        "ISIS-4820": {"name": "Ambientes interactivos 3D", "credits": 4, "summer": False},
        "ISIS-4216": {"name": "Inteligencia artificial y representación de conocimiento", "credits": 4,
                      "summer": False}}

    for codigo in cursosIsis:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MISIS"),
            code=codigo,
            credits=cursosIsis[codigo]["credits"],
            name=cursosIsis[codigo]["name"],
            summer=cursosIsis[codigo]["summer"])



#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MISO
    print "carga de cursos de MISO"
    cursosMiso = {
        "MISO4202": {"name": "Mejoramiento de la productividad: Automatización", "credits": 4, "summer": False},
        "MISO4204": {"name": "Fábricas de software y líneas de producto", "credits": 4, "summer": False},
        "MISO4205": {"name": "Mejoramiento de la experiencia del usuario", "credits": 4, "summer": False},
        "MISO4301": {"name": "Proyecto Integrador", "credits": 4, "summer": False},
        "MISO4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MISO4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MISO4205": {"name": "Mejoramiento de la experiencia del usuario", "credits": 4, "summer": False},
        "MISO4101": {"name": "Procesos de Desarrollo Ágiles", "credits": 4, "summer": False}}

    for codigo in cursosMiso:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MISIS"),
            code=codigo,
            credits=cursosMiso[codigo]["credits"],
            name=cursosMiso[codigo]["name"],
            summer=cursosMiso[codigo]["summer"])



    #Secciones de MISO
    print "carga de secciones de MISO"
    seccionesMiso = {
        14446: {"course": "MISO4101", "name": "1", "semester": 1, "year": 2015, "teacher": 79505041},
        13986: {"course": "MISO4202", "name": "1", "semester": 1, "year": 2015, "teacher": 000000001},
        14604: {"course": "MISO4204", "name": "1", "semester": 1, "year": 2015, "teacher": 79505041},
        16210: {"course": "MISO4205", "name": "1", "semester": 1, "year": 2015, "teacher": 000000002},
        16211: {"course": "MISO4301", "name": "1", "semester": 1, "year": 2015, "teacher": 000000003},
        15251: {"course": "MISO4302", "name": "1", "semester": 1, "year": 2015, "teacher": 000000004},
        16212: {"course": "MISO4303", "name": "1", "semester": 1, "year": 2015, "teacher": 000000004}}

    for seccion in seccionesMiso:
        add_section(
            crn=seccion,
            name=seccionesMiso[seccion]["name"],
            semester=seccionesMiso[seccion]["semester"],
            year=seccionesMiso[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMiso[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMiso[seccion]["course"])
        )


#-----------------------------------------------------------------------------------------------------------------------
#Metodo encargado de crear o dar un profesor
# params:   code => el codigo del profesor,
#           email => email del profesor, lastname => Apellido del profesor,
#           name => Nombre del profesor
def add_teacher(code, email, lastname, name):
    obj_teacher = Teacher.objects.get_or_create(code=code, email=email, lastname=lastname, name=name)[0]
    return obj_teacher


#Metodo encargado de crear una maestria
# params: name => nombre de la maestria
def add_master(name):
    p = Master.objects.get_or_create(name=name)[0]
    return p


def add_course(pensum, code, credits, name, summer):
    obj_course = Course.objects.get_or_create(code=code,
                                              credits=credits,
                                              name=name,
                                              summer=summer,
                                              pensum=pensum)[0]
    return obj_course


def add_section(crn, name, semester, year, teacher, course):
    obj_section = Section.objects.get_or_create(crn=crn,
                                                name=name,
                                                semester=semester,
                                                year=year,
                                                teacher=teacher,
                                                course=course)[0]
    return obj_section


#Metodo encargado en definir la creacion de un pensum
def add_pensum(name, active, master):
    if master != None:
        obj_pensum = Pensum.objects.get_or_create(name="Pensum_" + name,
                                                  active=active,
                                                  master=master)[0]
    return obj_pensum


# Start execution here!
if __name__ == '__main__':
    print "Iniciando población de datos base"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mati.settings')
    from map.models import Master, Pensum, Course, Teacher, Section

    populate()






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
