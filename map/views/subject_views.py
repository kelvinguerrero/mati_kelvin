from map.models import Subject, Student, Section
from django.shortcuts import render
from map.common.subject_common import list_subjects
from map.forms import SubjectForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required()
def subject(request, subject_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'GET':
        if subject_id == None:
            lista = list_subjects()
            return render(request, 'subject/subject_list.html', {'object_list': lista})
        else:
            ob_subject = Subject.objects.get(id=subject_id)
            return render(request, 'subject/subject_detail.html', {'object': ob_subject, 'detail': True})


def subject_edit(request, subject_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'GET':
        data = dict()
        if subject_id == None:
            form = SubjectForm()
            data.update({'form': form})
        else:
            subject = Subject.objects.get(id=subject_id)
            form = SubjectForm(initial={'grade': subject.grade,
                                        'student_status': subject.student_status,
                                        'student': subject.student.id,
                                        'section': subject.section.id,
                                        'id': subject.id})
            data.update({'object': subject, 'form': form})
        return render(request, 'subject/subject_form.html', data)
    elif request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('id'):
                # EDIT
                student = Subject.objects.get(id=form.cleaned_data['id'])
                student.grade = form.cleaned_data['grade']
                student.student_status = form.cleaned_data['student_status']
                student.student = form.cleaned_data['student']
                student.section = form.cleaned_data['section']
                student.save()
            else:
                # CREATE
                subject_obj = Student.objects.get(id=form.cleaned_data['student'])
                section_obj = Section.objects.get(id=form.cleaned_data['section'])
                form.cleaned_data['student']
                subject = Subject.objects.create(grade=form.cleaned_data['grade'],
                                                 student_status=form.cleaned_data['student_status'],
                                                 student=subject_obj,
                                                 section=section_obj
                                                 )
            return render(request, 'subject/subject_detail.html', {'object': subject, 'detail': True})
        else:
            # ENVIAR MENSAJE
            pass
    else:
        # ENVIAR MENSAJE DE REQUEST ERRONEO
        pass


def subject_delete(request, subject_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'GET':
        student = Subject.objects.get(id=subject_id)
        return render(request, 'subject/subject_confirm_delete.html', {'object': student, 'detail': True})
    elif request.method == 'POST':
        student_obj = Subject.objects.get(id=subject_id)
        if not student_obj == None:
            student_obj.delete()

        lista = list_subjects()
        return render(request, 'subject/subject_list.html', {'object_list':lista})