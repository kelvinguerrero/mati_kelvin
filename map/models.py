from django.db import models
from django.utils.timezone import now
# Create your models here.


class Pensum(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
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
    code = models.IntegerField()
    email = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
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
    code = models.IntegerField()
    email = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
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
    code = models.CharField(max_length=200)
    credits = models.IntegerField()
    name = models.CharField(max_length=200)
    summer = models.BooleanField(default=False)
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
            pensum=self.pensum
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
    crn = models.IntegerField()
    name = models.CharField(max_length=200)
    semester = models.IntegerField()
    year = models.IntegerField()
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
            teacher=self.teacher,
            course=self.course
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
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    student_status = models.BooleanField(default=False)
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
            grade=self.grade,
            student_status=self.student_status,
            student=self.student,
            section=self.section
        )

        return response