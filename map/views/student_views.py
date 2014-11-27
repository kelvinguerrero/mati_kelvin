from map.models import Student
from django.shortcuts import render
from map.common.student_common import list_students
from map.forms import StudentForm


def student(request, student_id=None):
    if request.method == 'GET':
        if student_id == None:
            lista = list_students()
            return render(request, 'student/student_list.html', {'object_list': lista})
        else:
            ob_student = Student.objects.get(id=student_id)
            return render(request, 'student/student_detail.html', {'object': ob_student, 'detail': True})


def student_edit(request, student_id=None):
    if request.method == 'GET':
        data = dict()
        if student_id == None:
            form = StudentForm()
            data.update({'form': form})
        else:
            student = Student.objects.get(id=student_id)
            form = StudentForm(initial={'code': student.code,
                                        'email': student.email,
                                        'lastname': student.lastname,
                                        'name': student.name,
                                        'student_status': student.student_status,
                                        'total_approved_credits': student.total_approved_credits,
                                        'total_credits_actual_semester': student.total_credits_actual_semester,
                                        'id': student.id})
            data.update({'object': student, 'form': form})
        return render(request, 'student/student_form.html', data)
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('id'):
                # EDIT
                student = Student.objects.get(id=form.cleaned_data['id'])
                student.code = form.cleaned_data['code']
                student.email = form.cleaned_data['email']
                student.lastname = form.cleaned_data['lastname']
                student.name = form.cleaned_data['name']
                student.student_status = form.cleaned_data['student_status']
                student.total_approved_credits = form.cleaned_data['total_approved_credits']
                student.total_credits_actual_semester = form.cleaned_data['total_credits_actual_semester']
                student.save()
            else:
                # CREATE
                student = Student.objects.create(code=form.cleaned_data['code'],
                                                 email=form.cleaned_data['email'],
                                                 lastname=form.cleaned_data['lastname'],
                                                 name=form.cleaned_data['name'],
                                                 student_status=form.cleaned_data['student_status'],
                                                 total_approved_credits=form.cleaned_data['total_approved_credits'],
                                                 total_credits_actual_semester=form.cleaned_data['total_credits_actual_semester']
                                                 )
            return render(request, 'student/student_detail.html', {'object': student, 'detail': True})
        else:
            # ENVIAR MENSAJE
            pass
    else:
        # ENVIAR MENSAJE DE REQUEST ERRONEO
        pass


def student_delete(request, student_id):
    if request.method == 'GET':
        student = Student.objects.get(id=student_id)
        return render(request, 'student/student_confirm_delete.html', {'object': student, 'detail': True})
    elif request.method == 'POST':
        student_obj = Student.objects.get(id=student_id)
        if not student_obj == None:
            student_obj.delete()

        lista = list_students()
        return render(request, 'student/student_list.html', {'object_list':lista})