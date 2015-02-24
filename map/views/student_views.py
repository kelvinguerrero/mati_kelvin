from map.models import Student, Master
from django.shortcuts import render
from map.common.student_common import list_students
from map.forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required()
def student(request, student_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            if student_id == None:
                lista = list_students()
                return render(request, 'student/student_list.html', {'object_list': lista})
            else:
                ob_student = Student.objects.get(id=student_id)

                return render(request, 'student/student_detail.html', {'object': ob_student, 'detail': True, 'code':ob_student.code})

@login_required()
def student_edit(request, student_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
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
                                            'master': student.master,
                                            'id': student.id})
                data.update({'object': student, 'form': form, 'code': student.code})
            return render(request, 'student/student_form.html', data)
        elif request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                if form.cleaned_data.get('id'):
                    # EDIT
                    ob_master = Master.objects.get(id=form.cleaned_data['master'])
                    student = Student.objects.get(id=form.cleaned_data['id'])
                    student.code = form.cleaned_data['code']
                    student.email = form.cleaned_data['email']
                    student.lastname = form.cleaned_data['lastname']
                    student.name = form.cleaned_data['name']
                    student.student_status = form.cleaned_data['student_status']
                    student.total_approved_credits = form.cleaned_data['total_approved_credits']
                    student.total_credits_actual_semester = form.cleaned_data['total_credits_actual_semester']
                    student.master = ob_master
                    student.save()
                else:
                    # CREATE
                    ob_master = Master.objects.get(id=form.cleaned_data['master'])
                    student = Student.objects.create(code=form.cleaned_data['code'],
                                                     email=form.cleaned_data['email'],
                                                     lastname=form.cleaned_data['lastname'],
                                                     name=form.cleaned_data['name'],
                                                     student_status=form.cleaned_data['student_status'],
                                                     total_approved_credits=form.cleaned_data['total_approved_credits'],
                                                     total_credits_actual_semester=form.cleaned_data['total_credits_actual_semester'],
                                                     master=ob_master
                                                     )
                    print(student.code)
                return render(request, 'student/student_detail.html', {'object': student, 'detail': True, 'code': student.code})
            else:
                # ENVIAR MENSAJE
                pass
        else:
            # ENVIAR MENSAJE DE REQUEST ERRONEO
            pass

@login_required()
def student_delete(request, student_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            student = Student.objects.get(id=student_id)
            print(student.code)
            return render(request, 'student/student_confirm_delete.html', {'object': student, 'detail': True, 'code':student.code})
        elif request.method == 'POST':
            student_obj = Student.objects.get(id=student_id)
            if not student_obj == None:
                student_obj.delete()

            lista = list_students()
            return render(request, 'student/student_list.html', {'object_list':lista})