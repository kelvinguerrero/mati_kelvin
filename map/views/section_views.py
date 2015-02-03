from map.models import Section, Teacher, Course
from django.shortcuts import render
from map.common.section_common import list_sections
from map.forms import SectionForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required()
def section(request, section_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            if section_id == None:
                lista = list_sections()
                return render(request, 'section/section_list.html', {'object_list': lista})
            else:
                ob_section = Section.objects.get(id=section_id)
                return render(request, 'section/section_detail.html', {'object': ob_section, 'detail': True})

@login_required()
def section_edit(request, section_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            data = dict()
            if section_id == None:
                form = SectionForm()
                data.update({'form':form})
            else:
                section = Section.objects.get(id=section_id)
                form = SectionForm(initial={'crn': section.crn,
                                            'name': section.name,
                                            'semester': section.semester,
                                            'year': section.year,
                                            'id': section.id})
                data.update({'object': section, 'form': form})
            return render(request, 'section/section_form.html', data)
        elif request.method == 'POST':
            form = SectionForm(request.POST)
            if form.is_valid():
                if form.cleaned_data.get('id'):
                    # EDIT
                    section = Section.objects.get(id=form.cleaned_data['id'])
                    section.crn = form.cleaned_data['crn']
                    section.name = form.cleaned_data['name']
                    section.semester = form.cleaned_data['semester']
                    section.year = form.cleaned_data['year']
                    section.save()
                else:
                    # CREATE
                    teacher_obj = Teacher.objects.get(id=form.cleaned_data['teacher'])
                    course_obj = Course.objects.get(id=form.cleaned_data['course'])
                    section = Section.objects.create(crn=form.cleaned_data['crn'],
                                                     name=form.cleaned_data['name'],
                                                     semester=form.cleaned_data['semester'],
                                                     year=form.cleaned_data['year'],
                                                     teacher=teacher_obj,
                                                     course=course_obj
                                                     )
                return render(request, 'section/section_detail.html', {'object': section, 'detail': True})
            else:
                # ENVIAR MENSAJE
                pass
        else:
            # ENVIAR MENSAJE DE REQUEST ERRONEO
            pass

@login_required()
def section_delete(request, section_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'GET':
        section = Section.objects.get(id=section_id)
        return render(request, 'section/section_confirm_delete.html', {'object':section, 'detail':True})
    elif request.method == 'POST':
        section_obj = Section.objects.get(id=section_id)
        if not section_obj == None:
            section_obj.delete()

        lista = list_sections()
        return render(request, 'section/section_list.html', {'object_list':lista})