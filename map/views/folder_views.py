from map.models import Course, Pensum, Student
from django.shortcuts import render
from map.common.folder_common import list_courses_scheme, calculate_credits, list_subject_approved
from map.forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required()
def folder(request, code_student_id=None):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            #if course_id == None:
            #    lista = list_courses()
            #    return render(request, 'folder/folder_list.html', {'object_list': lista})
            #else:
            lista = list_courses_scheme(student_code=code_student_id)
            lista_ap = list_subject_approved(student_code=code_student_id)
            creditos = calculate_credits(student_code=code_student_id)
            return render(request, 'folder/folder_detail.html', {'object_list': lista,
                                                                 'obj_cedits': creditos,
                                                                 'object_list_ap': lista_ap,
                                                                 'detail': True})

@login_required()
def folder_edit(request, course_id=None):
    print 'entrocurso'
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            data = dict()
            if course_id == None:
                form = CourseForm()
                data.update({'form': form})
            else:
                course = Course.objects.get(id=course_id)
                form = CourseForm(initial={'code': course.code,
                                           'credits': course.credits,
                                           'name': course.name,
                                           'summer': course.summer,
                                           'pensum': course.id,
                                           'id': course.id})
                data.update({'object': course, 'form': form})
            return render(request, 'course/course_form.html', data)
        elif request.method == 'POST':
            form = CourseForm(request.POST)
            if form.is_valid():

                if form.cleaned_data.get('id'):
                    # EDIT
                    pensum_obj = Pensum.objects.get(id=form.cleaned_data['pensum'])
                    course = Course.objects.get(id=form.cleaned_data['id'])

                    course.code = form.cleaned_data['code']
                    course.credits = form.cleaned_data['credits']
                    course.name = form.cleaned_data['name']
                    course.summer = form.cleaned_data['summer']
                    course.pensum = pensum_obj
                    course.save()
                else:
                    # CREATE
                    print 'entro',form.cleaned_data['pensum']
                    pensum_obj = Pensum.objects.get(id=form.cleaned_data['pensum'])

                    course = Course.objects.create(code=form.cleaned_data['code'],
                                                   credits=form.cleaned_data['credits'],
                                                   name=form.cleaned_data['name'],
                                                   summer=form.cleaned_data['summer'],
                                                   pensum=pensum_obj
                                                   )
                return render(request, 'course/course_detail.html', {'object': course, 'detail': True})
            else:
                # ENVIAR MENSAJE
                pass
        else:
            # ENVIAR MENSAJE DE REQUEST ERRONEO
            pass

@login_required()
def folder_delete(request, course_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            course = Course.objects.get(id=course_id)
            return render(request, 'course/course_confirm_delete.html', {'object': course, 'detail': True})
        elif request.method == 'POST':
            course_obj = Course.objects.get(id=course_id)
            if not course_obj == None:
                course_obj.delete()

            lista = list_courses()
            return render(request, 'course/course_list.html', {'object_list':lista})