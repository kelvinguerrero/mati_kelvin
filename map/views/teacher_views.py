from map.models import Teacher
from django.shortcuts import render
from map.common.teacher_common import list_teachers
from map.forms import TeacherForm


def teacher(request, teacher_id=None):
    if request.method == 'GET':
        if teacher_id == None:
            lista = list_teachers()
            return render(request, 'teacher/teacher_list.html', {'object_list': lista})
        else:
            ob_teacher = Teacher.objects.get(id=teacher_id)
            return render(request, 'teacher/teacher_detail.html', {'object': ob_teacher, 'detail': True})


def teacher_edit(request, teacher_id=None):
    if request.method == 'GET':
        data = dict()
        if teacher_id == None:
            form = TeacherForm()
            data.update({'form': form})
        else:
            teacher = Teacher.objects.get(id=teacher_id)
            form = TeacherForm(initial={'code': teacher.code,
                                        'email': teacher.email,
                                        'lastname': teacher.lastname,
                                        'name': teacher.name,
                                        'id': teacher.id})
            data.update({'object': teacher, 'form': form})
        return render(request, 'teacher/teacher_form.html', data)
    elif request.method == 'POST':
        form = TeacherForm(request.POST)
        print form
        if form.is_valid():
            if form.cleaned_data.get('id'):
                # EDIT
                teacher = Teacher.objects.get(id=form.cleaned_data['id'])
                teacher.code = form.cleaned_data['code']
                teacher.email = form.cleaned_data['email']
                teacher.lastname = form.cleaned_data['lastname']
                teacher.name = form.cleaned_data['name']
                teacher.save()
            else:
                # CREATE
                teacher = Teacher.objects.create(code=form.cleaned_data['code'],
                                                 email=form.cleaned_data['email'],
                                                 lastname=form.cleaned_data['lastname'],
                                                 name=form.cleaned_data['name'],
                                                 )
            return render(request, 'teacher/teacher_detail.html', {'object': teacher, 'detail': True})
        else:
            # ENVIAR MENSAJE
            pass
    else:
        # ENVIAR MENSAJE DE REQUEST ERRONEO
        pass


def teacher_delete(request, teacher_id):
    if request.method == 'GET':
        teacher = Teacher.objects.get(id=teacher_id)
        return render(request, 'teacher/teacher_confirm_delete.html', {'object': teacher, 'detail': True})
    elif request.method == 'POST':
        student_obj = Teacher.objects.get(id=teacher_id)
        if not student_obj == None:
            student_obj.delete()

        lista = list_teachers()
        return render(request, 'teacher/teacher_list.html', {'object_list':lista})