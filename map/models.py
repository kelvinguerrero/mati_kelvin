# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'
from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.utils.encoding import smart_unicode
import datetime
import jsonfield
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Modelos de la plataforma MAP
PRIMER_SEMESTRE = 10
SEGUNDO_SEMESTRE = 20
INTERSEMESTRAL = 18
VERANO = 19
SEMESTRE_CHOICES = (
    (PRIMER_SEMESTRE, 'primer_semestre'),
    (SEGUNDO_SEMESTRE, 'segundo_semestre'),
    (INTERSEMESTRAL, 'intersemestral'),
    (VERANO, 'verano'),
)


class Map(models.Model):
    semester = models.IntegerField(null=False, blank=False, unique=True, default=10, choices=SEMESTRE_CHOICES)
    year = models.IntegerField(null=False, blank=False, unique=True, default=datetime.date.today().year)


class Master(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )

    def __unicode__(self):
        return smart_unicode(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('map_master_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            name=self.name
        )

        return response


class Pensum(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    active = models.BooleanField(default=None, null=False, blank=False)
    master = models.ForeignKey('Master')
    created_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    def __unicode__(self):
        return smart_unicode(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('map_pensum_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id = self.id,
            name = self.name,
            active = self.active,
            master = self.master.to_dict()
        )

        return response


class Teacher(models.Model):
    code = models.IntegerField(null=False, blank=False, unique=True)
    email = models.CharField(max_length=200, null=True, blank=True, unique=True)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )

    def __unicode__(self):
        return smart_unicode(self.email)

    @models.permalink
    def get_absolute_url(self):
        return ('map_teacher_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            code=self.code,
            email=self.email,
            lastname=self.lastname,
            name=self.name
        )

        return response


  #//---------------------------------------------------------------------------------------------------------------//
  # Modelo que representa a un estudiante:
  #   Se modela los datos basicos del estudiante, el estado (student_status) el cual puede ser:
  #     * 1 Activo.
  #     * 2 Inactivo.
  #     * 3 Graduado.
  #
  #//---------------------------------------------------------------------------------------------------------------//
class Student(models.Model):
    code = models.IntegerField(null=False, blank=False, unique=True)
    email = models.CharField(max_length=200, null=True, blank=True, unique=True)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    student_status = models.IntegerField(default=1)
    scheme = models.OneToOneField('Scheme', on_delete=models.SET_NULL, related_name='Scheme', null=True, blank=True)
    master = models.ForeignKey('Master')
    created_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )

    def __unicode__(self):
        return smart_unicode(self.email)

    @models.permalink
    def get_absolute_url(self):
        return ('map_student_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            code=self.code,
            email=self.email,
            lastname=self.lastname,
            name=self.name,
            student_status=self.student_status,
            master=self.master.to_dict()
        )
        return response

    def to_dict_curriculum(self):
        response = dict()
        response.update(
            id=self.id,
            code=self.code,
            courses=self.course_set
        )
        return response


#Relacion que modela el plan de estudios que el estudiante crea
class Scheme(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    courses = models.ManyToManyField('Course', through='Scheme_courses')
    created_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    def __unicode__(self):
        return smart_unicode(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('map_pensum_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            name=self.name,
            #courses=[r.to_dict() for r in self.courses.all()]
            courses=agregar_cursos(self.courses.all(), self.id)
        )
        return response


def agregar_cursos(cursos_all, scheme_id):
    lista_cursos = list()
    for curso in cursos_all:
        sch_obj = Scheme_courses.objects.get(scheme_id=scheme_id, course_id= curso.id)
        print sch_obj.semester
        json_rta = {"curso": curso.to_dict(), "semestre": sch_obj.semester}
        lista_cursos.append(json_rta)

    print "salio"
    return lista_cursos


class Scheme_courses(models.Model):
    scheme = models.ForeignKey('Scheme')
    course = models.ForeignKey('Course')
    semester = models.IntegerField(null=True, blank=True)
    class Meta:
        unique_together = ("scheme", "course",)


class Course(models.Model):
    code = models.CharField(max_length=200, null=True, blank=True, unique=True)
    credits = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    summer = models.BooleanField(default=False, null=False, blank=False)
    pensum = models.ForeignKey('Pensum')

    created_at = models.DateTimeField(now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    def __unicode__(self):
        return smart_unicode(self.name + "" + self.code)

    @models.permalink
    def get_absolute_url(self):
        return ('map_course_detail', (), {'pk': self.pk})

    def to_dict_view(self):
        response = dict()
        response.update(
            id=self.id,
            code=self.code,
            name=self.name,
            credits=self.credits,
            summer=self.summer,
            pensum=self.pensum.to_dict()
        )
        return response

    def to_dict(self):
        response = dict()
        response.update(
            id=self.id,
            code=self.code,
            name=self.name,
            credits=self.credits,
            summer=self.summer,
            pensum=self.pensum.to_dict()
        )
        return response

    def to_dict_curriculum(self):
        response = dict()
        response.update(
            id=self.id,
            code=self.code,
            name=self.name,
            credits=self.credits
        )
        return response

    def to_dict_api(self):
        response = dict()
        response.update(
            id=self.id,
            code=self.code,
            name=self.name,
            credits=self.credits,
            summer=self.summer,
            pensum=self.pensum.id
        )
        return response


class Capacity(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    capacity = models.IntegerField(null=False, blank=False)
    section = models.ForeignKey('Section')

    created_at = models.DateTimeField(now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(now(),
        editable=False,
        null=True
    )
    def __unicode__(self):
        return smart_unicode(self.name + "" + str(self.capacity) )
    @models.permalink
    def get_absolute_url(self):
        return ('map_capacity_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            name=self.name,
            capacity=self.capacity
        )
        return response

EXECUTION = 0
PROPOSED = 1
DEVELOPED = 2
SECTION_STATUS_CHOICES = (
    (EXECUTION, 'Dictandose'),
    (PROPOSED, 'Propuesta'),
    (DEVELOPED, 'Dictada'),
)


class Section(models.Model):
    crn = models.IntegerField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    semester = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    teacher = models.ForeignKey('Teacher', null=True, blank=True)
    course = models.ForeignKey('Course')
    status = models.IntegerField(null=False, blank=False, choices=SECTION_STATUS_CHOICES)
    created_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    def __unicode__(self):
        return smart_unicode(self.name + " " + str(self.crn))
    @models.permalink
    def get_absolute_url(self):
        return ('map_section_detail',(),{'pk':self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            crn=self.crn,
            name=self.name,
            semester=self.semester,
            year=self.year,
            teacher=verificar_teacher(self),
            course=self.course.to_dict(),
            status=self.status,
            capacity=[r.to_dict() for r in self.capacity_set.all()]
        )

        return response

    def to_dict_sin_cap(self):
        response = dict()

        response.update(
            id=self.id,
            crn=self.crn,
            name=self.name,
            semester=self.semester,
            year=self.year,
            teacher=verificar_teacher(self),
            course=self.course.to_dict(),
            status=self.status,
        )

        return response


def verificar_teacher(self_obj):
    if self_obj.teacher == None:
        return "Sin aignar"
    else:
        self_obj.teacher.to_dict()


 #//---------------------------------------------------------------------------------------------------------------//
 # Modelo que representa el estado de la calificación de un estudiante:
 # Un estudiante inscribe una sección, y esta maneja una calificación por cada estudiante, esta calificación puede
 # estar dada por una nota ó puede ser aprobado o reprobado (true, false) respectivamente.
 #
 #   Dentro de este modelo se manejan los siguientes atributos:
 #     grade: Este campo modela la nota que obtuvo un estudiante
 #     subject_status: Este campo modela si el estudiante aprobo o repobo (true, false) respectivamente.
 #
 # El modelo contiene dos metodos que manejan el atributo de total_subject del estudiante.
 #   Cuando se crea un nuevo subject, suma el contador de total_subject del estudiante al que se creo el subject.
 #   Cuando se elimina un subject, en este caso se resta el contador total_subject del estudiante
 #//---------------------------------------------------------------------------------------------------------------//
class Subject(models.Model):
    grade = models.DecimalField(max_digits=10, decimal_places=5, null=False, blank=False)
    student_status = models.BooleanField(default=None, null=False, blank=False)
    student = models.ForeignKey('Student')
    section = models.ForeignKey('Section')
    created_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )

    @models.permalink
    def get_absolute_url(self):
        return ('map_subject_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()
        response.update(
            id=self.id,
            grade=str(self.grade),
            student_status=self.student_status,
            #student=verificar_student(self),
            section=verificar_section(self)
        )
        return response


def verificar_student(self_obj):
    if self_obj.student == None:
        return "Sin aignar"
    else:
        return self_obj.student.to_dict()


def verificar_section(self_obj):
    if self_obj.section == None:
        return "Sin aignar"
    else:
        return  self_obj.section.to_dict_sin_cap()


class Report(models.Model):
    name = models.CharField(max_length=200)
    json = jsonfield.JSONField({})
    master = models.IntegerField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )
    updated_at = models.DateTimeField(
        now(),
        editable=False,
        null=True
    )