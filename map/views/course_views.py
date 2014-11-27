from map.models import Course
from django.shortcuts import render
from map.common.course_common import list_courses
from map.forms import CourseForm
from django.views.generic import View

class CourseView(View):
    def get(self, request):
        return render(request, 'course/course_list.html')


def course(request, course_id=None):
    if request.method == 'GET':
        if course_id == None:
            lista = list_courses()
            return render(request, 'course/course_list.html', {'object_list': lista})
        else:
            ob_course = Course.objects.get(id=course_id)
            return render(request, 'course/course_detail.html', {'object': ob_course, 'detail': True})


def course_edit(request, course_id=None):
    if request.method == 'GET':
        data = dict()
        if course_id==None:
            form = CourseForm()
            data.update({'form': form})
        else:
            course = Course.objects.get(id=course_id)
            form = CourseForm(initial={'code': course.code,
                                       'credits': course.credits,
                                       'name': course.name,
                                       'summer': course.summer,
                                       'id': course.id})
            data.update({'object': course, 'form': form})
        return render(request, 'course/course_form.html', data)
    elif request.method == 'POST':
        form = CourseForm(request.POST)
        print form
        if form.is_valid():
            print 'entro'
            if form.cleaned_data.get('id'):
                # EDIT
                course = Course.objects.get(id=form.cleaned_data['id'])
                course.name = form.cleaned_data['code']
                course.credits = form.cleaned_data['credits']
                course.name = form.cleaned_data['name']
                course.summer = form.cleaned_data['summer']
                course.save()
            else:
                # CREATE
                course = Course.objects.create(name=form.cleaned_data['name'], active=form.cleaned_data['active'])
            return render(request, 'course/course_detail.html', {'object': course, 'detail': True})
        else:
            # ENVIAR MENSAJE
            pass
    else:
        # ENVIAR MENSAJE DE REQUEST ERRONEO
        pass


def course_delete(request, course_id):
    if request.method == 'GET':
        course = Course.objects.get(id=course_id)
        return render(request, 'course/course_confirm_delete.html', {'object': course, 'detail': True})
    elif request.method == 'POST':
        course_obj = Course.objects.get(id=course_id)
        if not course_obj == None:
            course_obj.delete()

        lista = list_courses()
        return render(request, 'course/course_list.html', {'object_list':lista})