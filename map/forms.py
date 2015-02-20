from django import forms
from django.forms import widgets


class MasterForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    name = forms.CharField(label='Nombre', required=True)
    name.widget.attrs = {'class': 'form-control', 'required': True}


class PensumForm(forms.Form):

    id = forms.CharField(widget=widgets.HiddenInput, required=False)

    name = forms.CharField(label='Nombre', required=True)
    name.widget.attrs = {'class': 'form-control', 'required': True}

    active = forms.BooleanField(label='Activo', required=False)

    master = forms.IntegerField(label='Master')
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

    master = forms.IntegerField(label='Master')
    master.widget.attrs = {'class': 'form-control', 'required': True}


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