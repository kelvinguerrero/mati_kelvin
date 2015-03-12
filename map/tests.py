

__author__ = 'kelvin Guerrero'

from django.test import TestCase
from map.models import *
from common.master_common import *
from common.pensum_common import *
from common.teacher_common import *
from common.student_common import *
from common.course_common import *
from common.section_common import *
from django.core.urlresolvers import reverse
from populate_db import populate
import json
import urllib
import urllib2


#Pruebas unitarias para el los servicios estudiante
class MasterTest(TestCase):
    def create_master(self, name="test Master"):
        return Master.objects.create(name=name)

    def test_master_creation(self):
        obj = self.create_master()
        self.assertTrue(isinstance(obj, Master))
        self.assertEqual(obj.__unicode__(), obj.name)

    def test_master_view(self):
        url = reverse('master')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        rev=reverse('pensum_api')
        resp2 = self.client.get(rev)
        self.assertEqual(resp2.status_code, 500)

    def test_dar_maestria(self):
        lista_masters = list_masters()
        for obj_master in lista_masters:
            id= obj_master.id
            obj_mas=dar_maestria(id)
            self.assertEqual(obj_mas.name, obj_master.name)

    def test_dar_dict_maestrias(self):
        obj = self.create_master()
        self.assertTrue(obj.to_dict().__contains__("name"))

    def test_dar_dict_maestrias(self):
        obj = crear_maestria("testMaster")
        self.assertTrue(obj.name=="testMaster")


#Pruebas unitarias para el los servicios pensum
class PensumTest(TestCase):

    def create_pensum(self, name="pensumTest", active=True, master="masterTest"):
        p = Master.objects.get_or_create(name=master)[0]
        if p!= None:
            obj_pensum = Pensum.objects.get_or_create(name=name,
                                                      active=active,
                                                      master=p)[0]
            self.pensumInstance = obj_pensum
            return obj_pensum
        return None

    def test_pensum_creation(self):
        obj = self.create_pensum()
        self.assertTrue(isinstance(obj, Pensum))
        self.assertEqual(obj.__unicode__(), obj.name)
        self.assertEqual(obj.name, obj.name)
        self.assertEqual(obj.active, obj.active)
        self.assertEqual(obj.master.name, obj.master.name)

    def test_pensum_view(self):
        url = reverse('pensum')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        rev=reverse('pensum_api')
        resp2 = self.client.get(rev)
        self.assertEqual(resp2.status_code, 500)

    def test_dar_pensum(self):
        lista_masters = list_pensums()
        for obj_master in lista_masters:
            id= obj_master.id
            obj_mas=dar_pensum(id)
            self.assertEqual(obj_mas.name, obj_master.name)
            self.assertEqual(obj_mas.active, obj_master.active)

    def test_dar_dict_pensum(self):
        obj = self.create_pensum()
        self.assertTrue(obj.to_dict().__contains__("name"))
        self.assertTrue(obj.to_dict().__contains__("active"))
        self.assertTrue(obj.to_dict().__contains__("name"))


#Pruebas unitarias para el los servicios pensum
class TeacherTest(TestCase):

    def create_teacher(self, code="0001", email="emailTest", lastname="lastNameTest", name="teachertest"):
        obj_teacher = Teacher.objects.get_or_create(code=code, email=email, lastname=lastname, name=name)[0]
        if obj_teacher!=None:
            return obj_teacher
        return None

    def test_teacher_creation(self):
        obj = self.create_teacher()
        self.assertTrue(isinstance(obj, Teacher))
        self.assertEqual(obj.__unicode__(), obj.email)
        self.assertEqual(obj.code, obj.code)
        self.assertEqual(obj.email, obj.email)
        self.assertEqual(obj.lastname, obj.lastname)
        self.assertEqual(obj.name, obj.name)

    def test_teacher_view(self):
        url = reverse('teacher')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        rev=reverse('teacher_api')
        resp2 = self.client.get(rev)
        self.assertEqual(resp2.status_code, 500)

    def test_dar_teacher(self):
        lista_masters = list_teachers()
        for obj_master in lista_masters:
            id= obj_master.id
            obj_mas=dar_teachers(id)
            self.assertEqual(obj_mas.code, obj_master.code)
            self.assertEqual(obj_mas.email, obj_master.email)
            self.assertEqual(obj_mas.lastname, obj_master.lastname)
            self.assertEqual(obj_mas.name, obj_master.name)

    def test_dar_dict_teacher(self):
        obj = self.create_teacher()
        self.assertTrue(obj.to_dict().__contains__("code"))
        self.assertTrue(obj.to_dict().__contains__("email"))
        self.assertTrue(obj.to_dict().__contains__("name"))
        self.assertTrue(obj.to_dict().__contains__("lastname"))


#Pruebas unitarias para el los servicios estudiante
class StudentTest(TestCase):

    def create_master_Student(self, name="test master"):
        obj_student = Master.objects.get_or_create(name=name)[0]
        return obj_student

    def create_student(self, code=01, email="test@test.com", lastname="testlastName", name="testName"):
        obj_master = self.create_master_Student()
        return Student.objects.create(code=code,
                                      email=email,
                                      lastname=lastname,
                                      name=name,
                                      master=obj_master)

    def test_student_creation(self):
        obj = self.create_student()
        self.assertTrue(isinstance(obj, Student))
        self.assertEqual(obj.__unicode__(), obj.email)
        self.assertEqual(obj.code, obj.code)
        self.assertEqual(obj.email, obj.email)
        self.assertEqual(obj.lastname, obj.lastname)
        self.assertEqual(obj.name, obj.name)
        self.assertEqual(obj.student_status, obj.student_status)

    def test_student_view(self):
        url = reverse('student')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        rev=reverse('student_api')
        resp2 = self.client.get(rev)
        self.assertEqual(resp2.status_code, 500)

    def test_dar_student(self):
        lista_masters = list_students()
        for obj_master in lista_masters:
            id= obj_master.id
            obj_mas=dar_estudiante(id)
            self.assertEqual(obj_mas.code, obj_master.code)
            self.assertEqual(obj_mas.email, obj_master.email)
            self.assertEqual(obj_mas.lastname, obj_master.lastname)
            self.assertEqual(obj_mas.name, obj_master.name)

    def test_dar_dict_student(self):
        obj = self.create_student()
        self.assertTrue(obj.to_dict().__contains__("code"))
        self.assertTrue(obj.to_dict().__contains__("email"))
        self.assertTrue(obj.to_dict().__contains__("lastname"))
        self.assertTrue(obj.to_dict().__contains__("name"))
        self.assertTrue(obj.to_dict().__contains__("student_status"))


#Pruebas unitarias para el los servicios pensum
class SchemeTest(TestCase):

    def create_master_scheme(self, name="test Master"):
        return Master.objects.get_or_create(name=name)[0]

    def create_student(self, code=01, email="test@test.com", lastname="testlast Name", name="test Name"):
        obj_master = self.create_master_scheme()
        return Student.objects.create(code=code,
                                      email=email,
                                      lastname=lastname,
                                      name=name,
                                      master=obj_master)

    def create_pensum(self, name="pensumTest", active=True, master="testmaster"):
        p = Master.objects.get_or_create(name=master)[0]
        if p!= None:
            obj_pensum = Pensum.objects.get_or_create(name=name,
                                                      active=active,
                                                      master=p)[0]
            self.pensumInstance = obj_pensum
            return obj_pensum
        return None

    def create_course(self, code="test001", credits=4, name="testStudent", summer=False):
        pensum = self.create_pensum()
        return Course.objects.get_or_create(code=code,
                                              credits=credits,
                                              name=name,
                                              summer=summer,
                                              pensum=pensum)[0]

    def add_couse_scheme(self, scheme, planEstudio):
        i=1
        student_obj = self.create_student()
        for cursos in planEstudio:
            i=i+1
            curso_obj = self.create_course(code=cursos)
            scheme.courses.add(curso_obj)
            student_obj.scheme = scheme
            student_obj.save()

    def create_scheme(self, name="schemetest"):
        planEstudio = {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" }
        obj_scheme = Scheme.objects.get_or_create(name=name)[0]
        if obj_scheme!=None:
            self.add_couse_scheme(obj_scheme, planEstudio)
        return obj_scheme

    def test_scheme_creation(self):
        obj = self.create_scheme()
        self.assertTrue(isinstance(obj, Scheme))
        self.assertEqual(obj.__unicode__(), obj.name)
        self.assertEqual(obj.name, obj.name)

    def test_teacher_view(self):
        url = reverse('teacher')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        rev=reverse('teacher_api')
        resp2 = self.client.get(rev)
        self.assertEqual(resp2.status_code, 500)

    def test_dar_dict_student(self):
        obj = self.create_scheme()
        self.assertTrue(obj.to_dict().__contains__("name"))


#Pruebas unitarias para el los servicios Course
class CourseTest(TestCase):

    def create_pensum(self, name="pensumTest", active=True, master="masterTest"):
        p = Master.objects.get_or_create(name=master)[0]
        if p!= None:
            obj_pensum = Pensum.objects.get_or_create(name=name,
                                                      active=active,
                                                      master=p)[0]
            self.pensumInstance = obj_pensum
            return obj_pensum
        return None

    def create_course(self, code="test001", credits=4, name="testStudent", summer=False):
        pensum = self.create_pensum()
        return Course.objects.get_or_create(code=code,
                                              credits=credits,
                                              name=name,
                                              summer=summer,
                                              pensum=pensum)[0]

    def test_course_creation(self):
        obj = self.create_course()
        self.assertTrue(isinstance(obj, Course))
        self.assertEqual(obj.__unicode__(), obj.name+""+obj.code)
        self.assertEqual(obj.code, obj.code)
        self.assertEqual(obj.credits, obj.credits)
        self.assertEqual(obj.name, obj.name)
        self.assertEqual(obj.summer, obj.summer)

    def test_course_view(self):
        url = reverse('course')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        rev=reverse('course_api')
        resp2 = self.client.get(rev)
        self.assertEqual(resp2.status_code, 500)

    def test_dar_course(self):
        lista_masters = list_courses()
        for obj_master in lista_masters:
            id= obj_master.id
            obj_mas=dar_curso_by_id(id)
            self.assertEqual(obj_mas.code, obj_master.code)
            self.assertEqual(obj_mas.credits, obj_master.credits)
            self.assertEqual(obj_mas.summer, obj_master.summer)
            self.assertEqual(obj_mas.name, obj_master.name)

    def test_dar_secciones_curso(self):
        lista_masters = list_courses()
        for obj_master in lista_masters:
            self.assertTrue(obj_master.__contains__("code"))
            self.assertTrue(obj_master.__contains__("name"))
            self.assertTrue(obj_master.__contains__("credits"))
            self.assertTrue(obj_master.__contains__("summer"))

    def test_dar_secciones_curso(self):
        lista_masters = list_courses_api()
        for obj_master in lista_masters:
            self.assertTrue(obj_master.__contains__("code"))
            self.assertTrue(obj_master.__contains__("name"))
            self.assertTrue(obj_master.__contains__("credits"))
            self.assertTrue(obj_master.__contains__("summer"))

    def test_dar_curso_by_code(self):
        obj = self.create_course()
        obj_code = dar_curso_by_code(obj.code)
        self.assertTrue(isinstance(obj_code, Course))
        self.assertTrue(obj_code.code == obj.code)


    def test_dar_curso_by_id(self):
        obj = self.create_course()
        obj_code = dar_curso_by_id(obj.id)
        self.assertTrue(isinstance(obj_code, Course))
        self.assertTrue(obj_code.id == obj.id)



    def test_dar_dict_curso(self):
        obj = self.create_course()
        self.assertTrue(obj.to_dict().__contains__("code"))
        self.assertTrue(obj.to_dict().__contains__("name"))
        self.assertTrue(obj.to_dict().__contains__("credits"))
        self.assertTrue(obj.to_dict().__contains__("summer"))

    def test_dar_dict_curso(self):
        obj = self.create_course()
        self.assertTrue(obj.to_dict_api().__contains__("code"))
        self.assertTrue(obj.to_dict_api().__contains__("name"))
        self.assertTrue(obj.to_dict_api().__contains__("credits"))
        self.assertTrue(obj.to_dict_api().__contains__("summer"))

    def test_crear_curso(self):
        pens=self.create_pensum()
        obj_creado = crear_curso("code_test",True,"nombre",3,pens)
        self.assertTrue(obj_creado.to_dict_api().__contains__("code"))
        self.assertTrue(obj_creado.to_dict_api().__contains__("name"))
        self.assertTrue(obj_creado.to_dict_api().__contains__("credits"))
        self.assertTrue(obj_creado.to_dict_api().__contains__("summer"))

    def test_crear_curso(self):
        course=self.create_course()
        dar_secciones(course.id)



#Pruebas unitarias para el los servicios Course
class SectionTest(TestCase):

    def create_pensum(self, name="pensumTest", active=True, master="masterTest"):
        p = Master.objects.get_or_create(name=master)[0]
        if p!= None:
            obj_pensum = Pensum.objects.get_or_create(name=name,
                                                      active=active,
                                                      master=p)[0]
            self.pensumInstance = obj_pensum
            return obj_pensum
        return None

    def create_course(self, code="test001", credits=4, name="testStudent", summer=False):
        pensum = self.create_pensum()
        return Course.objects.get_or_create(code=code,
                                              credits=credits,
                                              name=name,
                                              summer=summer,
                                              pensum=pensum)[0]

    def create_teacher(self, code="0001", email="emailTest", lastname="lastNameTest", name="teachertest"):
        obj_teacher = Teacher.objects.get_or_create(code=code, email=email, lastname=lastname, name=name)[0]
        if obj_teacher!=None:
            return obj_teacher
        return None

    def create_section(self, crn=001, name="testStudent", semester=1,year=2015,status=1):
        obj_teacher = self.create_teacher()
        obj_course = self.create_course()
        obj_section = Section.objects.get_or_create(crn=crn,
                                                name=name,
                                                semester=semester,
                                                year=year,
                                                teacher=obj_teacher,
                                                course=obj_course,
                                                status=status)[0]
        return obj_section

    def test_section_creation(self):
        obj = self.create_section()
        self.assertTrue(isinstance(obj, Section))
        self.assertEqual(obj.__unicode__(), obj.name+" "+str(obj.crn))
        self.assertEqual(obj.crn, obj.crn)
        self.assertEqual(obj.name, obj.name)
        self.assertEqual(obj.semester, obj.semester)
        self.assertEqual(obj.year, obj.year)
        self.assertEqual(obj.status, obj.status)

    def test_section_view(self):
        url = reverse('section')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        rev=reverse('section_api')
        resp2 = self.client.get(rev)
        self.assertEqual(resp2.status_code, 500)

    def test_dar_section(self):
        lista_masters = list_sections()
        for obj_master in lista_masters:
            id= obj_master.id
            obj_mas=dar_seccion(id)
            self.assertEqual(obj_mas.crn, obj_master.code)
            self.assertEqual(obj_mas.name, obj_master.name)
            self.assertEqual(obj_mas.year, obj_master.year)
            self.assertEqual(obj_mas.status, obj_master.status)

    def test_dar_dict_section(self):
        obj = self.create_section()
        self.assertTrue(obj.to_dict().__contains__("crn"))
        self.assertTrue(obj.to_dict().__contains__("name"))
        self.assertTrue(obj.to_dict().__contains__("semester"))
        self.assertTrue(obj.to_dict().__contains__("year"))
        self.assertTrue(obj.to_dict().__contains__("status"))