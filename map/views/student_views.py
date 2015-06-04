from map.models import Student, Master
from django.shortcuts import render
from map.common.student_common import list_students, dar_estudiante_codigo, crear_plan_studios
from map.forms import StudentForm, darEstudianteForm, crearPlanEstudianteForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from map.common.folder_common import list_courses_scheme, \
                                     list_subject_approved

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
                list_courses = list_courses_scheme(ob_student.code)
                print(list_courses)
                list_subject = list_subject_approved(ob_student.code)
                if list_courses != None:
                        list_courses=list_courses.to_dict()
                return render(request, 'student/student_detail.html', {'object': ob_student,
                                                                       'detail': True,
                                                                       'list_courses': list_courses,
                                                                       'list_subject': list_subject,
                                                                       'code': ob_student.code})

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

@login_required()
def dar_estudiante(request, student_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            form = darEstudianteForm()
            return render(request, 'student/dar_student_form.html', {'form': form})
        if request.method == 'POST':
            form = darEstudianteForm(request.POST)
            if form.is_valid():
                estudiante_code = form.cleaned_data['estudiante_code']
                ob_student = dar_estudiante_codigo(estudiante_code)
                list_courses = list_courses_scheme(ob_student.code)
                list_subject = list_subject_approved(ob_student.code)


                if list_courses != None:
                        list_courses=list_courses.to_dict()
                print list_courses
                print(list_courses)
                return render(request, 'student/student_detail.html', {'object': ob_student,
                                                                       'detail': True,
                                                                       'list_courses': list_courses,
                                                                       'list_subject': list_subject,
                                                                       'code': ob_student.code})


@login_required()
def crear_plan_estudiante(request, student_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            data = dict()
            curso_1 = ''
            curso_2 = ''
            curso_3 = ''
            curso_4 = ''
            curso_5 = ''
            curso_6 = ''
            curso_7 = ''
            curso_8 = ''
            curso_9 = ''
            curso_10 = ''

            if student_id == None:
                lista = list_students()
                return render(request, 'student/student_list.html', {'object_list': lista})
            else:
                student = Student.objects.get(id=student_id)
                list_courses = list_courses_scheme(student.code)
                print list_courses
                if list_courses:
                    if list_courses != None:
                        list_courses=list_courses.to_dict()
                    for curso in list_courses["courses"]:

                        if curso["semestre"] == 1:
                            curso_1 = curso["curso"]["code"]
                        elif curso["semestre"] == 2:
                            curso_2 = curso["curso"]["code"]
                        elif curso["semestre"] == 3:
                            curso_3 = curso["curso"]["code"]
                        elif curso["semestre"] == 4:
                            curso_4 = curso["curso"]["code"]
                        elif curso["semestre"] == 5:
                            curso_5 = curso["curso"]["code"]
                        elif curso["semestre"] == 6:
                            curso_6 = curso["curso"]["code"]
                        elif curso["semestre"] == 7:
                            curso_7 = curso["curso"]["code"]
                        elif curso["semestre"] == 8:
                            curso_8 = curso["curso"]["code"]
                        elif curso["semestre"] == 9:
                            curso_9 = curso["curso"]["code"]
                        elif curso["semestre"] == 10:
                            curso_10 = curso["curso"]["code"]

                form = crearPlanEstudianteForm(initial={'curso_1': curso_1,
                                                        'curso_2': curso_2,
                                                        'curso_3': curso_3,
                                                        'curso_4': curso_4,
                                                        'curso_5': curso_5,
                                                        'curso_6': curso_6,
                                                        'curso_7': curso_7,
                                                        'curso_8': curso_8,
                                                        'curso_9': curso_9,
                                                        'curso_10': curso_10})

                data.update({'object': student,'id_student': student.id, 'form': form, 'code': student.code})
                return render(request, 'student/crear_plan_student_form.html', data)
        if request.method == 'POST':
            form = crearPlanEstudianteForm(request.POST)
            if form.is_valid():
                estdiante = Student.objects.get(id=student_id)
                crear_plan_studios(student_id,
                                    "plan"+str(estdiante.code),
                                    form.cleaned_data['curso_1'],
                                    form.cleaned_data['curso_2'],
                                    form.cleaned_data['curso_3'],
                                    form.cleaned_data['curso_4'],
                                    form.cleaned_data['curso_5'],
                                    form.cleaned_data['curso_6'],
                                    form.cleaned_data['curso_7'],
                                    form.cleaned_data['curso_8'],
                                    form.cleaned_data['curso_9'],
                                    form.cleaned_data['curso_10'])
                list_courses = list_courses_scheme(estdiante.code)
                list_subject = list_subject_approved(estdiante.code)
                if list_courses != None:
                        list_courses=list_courses.to_dict()
                return render(request, 'student/student_detail.html', {'object': estdiante,
                                                                       'detail': True,
                                                                       'list_courses': list_courses,
                                                                       'list_subject': list_subject,
                                                                       'code': estdiante.code})