__author__ = 'kelvin Guerrero'
from django.db import models
from django.utils.timezone import now
from django.utils.encoding import smart_unicode
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your models here.


class Pensum(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    active = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
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
            active = self.active
        )

        return response


class Teacher(models.Model):
    code = models.IntegerField(null=False, blank=False, unique=True)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
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


class Student(models.Model):
    code = models.IntegerField(null=False, blank=False, unique=True)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    student_status = models.IntegerField()
    total_approved_credits = models.IntegerField()
    total_credits_actual_semester = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
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
            total_approved_credits=self.total_approved_credits,
            total_credits_actual_semester=self.total_credits_actual_semester
        )

        return response


class Course(models.Model):
    code = models.CharField(max_length=200, null=False, blank=False)
    credits = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    summer = models.BooleanField(default=False, null=False, blank=False)
    pensum = models.ForeignKey('Pensum')
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )
    def __unicode__(self):
        return smart_unicode(self.name + "" + self.code)

    @models.permalink
    def get_absolute_url(self):
        return ('map_course_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            code=self.code,
            name=self.name,
            credits=self.credits,
            summer=self.summer,
            pensum=json.dumps(self.pensum.to_dict(), cls=DjangoJSONEncoder)
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


class Section(models.Model):
    crn = models.IntegerField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    semester = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    teacher = models.ForeignKey('Teacher')
    course = models.ForeignKey('Course')
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )
    def __unicode__(self):
        return smart_unicode(self.name + " " + self.crn )
    @models.permalink
    def get_absolute_url(self):
        return ('map_section_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            crn=self.crn,
            name=self.name,
            semester=self.semester,
            year=self.year,
            teacher=json.dumps(self.teacher.to_dict()),
            course=json.dumps(self.course.to_dict())
        )

        return response

    def to_dict_api(self):
        response = dict()

        response.update(
            id=self.id,
            crn=self.crn,
            name=self.name,
            semester=self.semester,
            year=self.year,
            teacher=self.teacher.id,
            course=self.course.id
        )

        return response


class Subject(models.Model):
    grade = models.DecimalField(max_digits=10, decimal_places=5, null=False, blank=False)
    student_status = models.BooleanField(default=False, null=False, blank=False)
    student = models.ForeignKey('Student')
    section = models.ForeignKey('Section')
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('map_subject_detail', (), {'pk': self.pk})

    def to_dict(self):
        response = dict()

        response.update(
            id=self.id,
            grade=json.dumps(self.grade, cls=DjangoJSONEncoder),
            section=json.dumps(self.section.to_dict())
        )

        return response

