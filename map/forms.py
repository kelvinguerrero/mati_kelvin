# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory
from django.forms import widgets
from map.models import Master, Course


class MasterForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    name = forms.CharField(label='Nombre', required=True)
    name.widget.attrs = {'class': 'form-control', 'required': True}


class MaterCarpetaForm(forms.Form):
    codigo = forms.IntegerField(label='Codigo del estudiante')
    codigo.widget.attrs = {'class': 'form-control', 'required': True}


class MaterStudentCourseForm(forms.Form):
    codigo = forms.IntegerField(label='Codigo del estudiante')
    codigo.widget.attrs = {'class': 'form-control', 'required': True}
    curso = forms.CharField(label='Codigo del curso')
    curso.widget.attrs = {'class': 'form-control', 'required': True}


class darStudentMasterForm(forms.Form):

    query = Master.objects.all()
    maestria = forms.ModelChoiceField(queryset=query.order_by('name'))
    maestria.widget.attrs = {'class': 'form-control', 'required': True}


class darCourseForm(forms.Form):
    curso = forms.CharField(label='Código curso', required=True)
    curso.widget.attrs = {'class': 'form-control', 'required': True}


class darEstudianteForm(forms.Form):
    estudiante_code = forms.CharField(label='Código del estudiante', required=True)
    estudiante_code.widget.attrs = {'class': 'form-control', 'required': True}


class crearPlanEstudianteForm(forms.Form):

    curso_1 = forms.CharField(label='Código del curso del semestre 1', required=True)
    curso_1.widget.attrs = {'class': 'form-control', 'required': True}

    curso_2= forms.CharField(label='Código del curso del semestre 2', required=True)
    curso_2.widget.attrs = {'class': 'form-control', 'required': True}

    curso_3= forms.CharField(label='Código del curso del semestre 3', required=True)
    curso_3.widget.attrs = {'class': 'form-control', 'required': True}

    curso_4 = forms.CharField(label='Código del curso del semestre 4', required=True)
    curso_4.widget.attrs = {'class': 'form-control', 'required': True}

    curso_5 = forms.CharField(label='Código del curso del semestre 5', required=True)
    curso_5.widget.attrs = {'class': 'form-control', 'required': True}

    curso_6 = forms.CharField(label='Código del curso del semestre 6', required=True)
    curso_6.widget.attrs = {'class': 'form-control', 'required': True}

    curso_7 = forms.CharField(label='Código del curso del semestre 7', required=True)
    curso_7.widget.attrs = {'class': 'form-control', 'required': True}

    curso_8 = forms.CharField(label='Código del curso del semestre 8', required=True)
    curso_8.widget.attrs = {'class': 'form-control', 'required': True}

    curso_9 = forms.CharField(label='Código del curso del semestre 9', required=True)
    curso_9.widget.attrs = {'class': 'form-control', 'required': True}

    curso_10 = forms.CharField(label='Código del curso del semestre 10', required=True)
    curso_10.widget.attrs = {'class': 'form-control', 'required': True}


class darSeccionForm(forms.Form):
    seccion_crn = forms.CharField(label='Crn de la sección', required=True)
    seccion_crn.widget.attrs = {'class': 'form-control', 'required': True}


class PensumForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    name = forms.CharField(label='Nombre', required=True)
    name.widget.attrs = {'class': 'form-control', 'required': True}

    active = forms.BooleanField(label='Activo', required=False)

    master = forms.CharField(label='Master')
    master.widget.attrs = {'class': 'form-control', 'required': True}


class CourseForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    code = forms.CharField(label='Codigo')
    code.widget.attrs = {'class': 'form-control', 'required': True}

    credits = forms.IntegerField(label='Creditos')
    credits.widget.attrs = {'class': 'form-control', 'required': True}

    name = forms.CharField(label='Nombre')
    name.widget.attrs = {'class': 'form-control', 'required': True}

    summer = forms.BooleanField(label='Vacacional', required=False)

    pensum = forms.IntegerField(label='Pensum')
    pensum.widget.attrs = {'class': 'form-control', 'required': True}


class SectionForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    crn = forms.CharField(label='crn')
    crn.widget.attrs = {'class': 'form-control', 'required': True}

    name = forms.CharField(label='Nombre')
    name.widget.attrs = {'class': 'form-control', 'required': True}

    semester = forms.IntegerField(label='Semestre')
    semester.widget.attrs = {'class': 'form-control', 'required': True}

    year = forms.IntegerField(label='Ano')
    year.widget.attrs = {'class': 'form-control', 'required': True}

    teacher = forms.IntegerField(label='Profesor')
    teacher.widget.attrs = {'class': 'form-control', 'required': True}

    course = forms.IntegerField(label='Curso')
    course.widget.attrs = {'class': 'form-control', 'required': True}


class StudentForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    code = forms.IntegerField(label='Codigo')
    code.widget.attrs = {'class': 'form-control', 'required': True}

    email = forms.CharField(label='Correo')
    email.widget.attrs = {'class': 'form-control', 'required': True}

    lastname = forms.CharField(label='Apellido')
    lastname.widget.attrs = {'class': 'form-control', 'required': True}

    name = forms.CharField(label='Nombre')
    name.widget.attrs = {'class': 'form-control', 'required': True}

    student_status = forms.IntegerField(label='Estado del estudiante')
    student_status.widget.attrs = {'class': 'form-control', 'required': True}

    total_approved_credits = forms.IntegerField(label='T. de creditos aprobados')
    total_approved_credits.widget.attrs = {'class': 'form-control', 'required': True}

    total_credits_actual_semester = forms.IntegerField(label='T. creditos semestre actual')
    total_credits_actual_semester.widget.attrs = {'class': 'form-control', 'required': True}

    master = forms.CharField(label='Master')
    master.widget.attrs = {'class': 'form-control', 'required': True}


class Courses_student_form(forms.ModelForm):
    course = forms.MultipleChoiceField(choices={})


class TeacherForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    code = forms.IntegerField(label='Codigo')
    code.widget.attrs = {'class': 'form-control', 'required': True}

    email = forms.CharField(label='Correo')
    email.widget.attrs = {'class': 'form-control', 'required': True}

    lastname = forms.CharField(label='Apellido')
    lastname.widget.attrs = {'class': 'form-control', 'required': True}

    name = forms.CharField(label='Nombre')
    name.widget.attrs = {'class': 'form-control', 'required': True}


class SubjectForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    grade = forms.IntegerField(label='Nota')
    grade.widget.attrs = {'class': 'form-control', 'required': True}

    student_status = forms.BooleanField(label='Estado del estudiante', required=False)

    student = forms.IntegerField(label='Estudiante')
    student.widget.attrs = {'class': 'form-control', 'required': True}

    section = forms.IntegerField(label='Seccion')
    section.widget.attrs = {'class': 'form-control', 'required': True}