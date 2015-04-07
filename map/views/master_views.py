from map.models import Master
from django.shortcuts import render
from map.common.master_common import list_masters, dar_maestria_nombre, dar_estudiantes_proyecto_grado
from map.common.folder_common import structure_master_courses, \
                                     calculate_credits, \
                                     list_courses_scheme, \
                                     list_subject_approved
from map.common.student_common import   dar_estudiante_codigo, \
                                        dar_maestria_de_estudiante, \
                                        ingles_aprobado,\
                                        tiene_cruso
from map.forms import MasterForm, MaterCarpetaForm, MaterStudentCourseForm, darStudentMasterForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import json


class MasterView(View):

    def get(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/')
        return render(request, 'master/master_list.html')

@login_required()
def master(request, master_id=None):
    if not request.user.is_authenticated():
        print "entro login"
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            if master_id is None:
                print "entro Mater"
                lista = list_masters()
                return render(request, 'master/master_list.html', {'object_list': lista})
            else:
                ob_master = Master.objects.get(id=master_id)
                return render(request, 'master/master_detail.html', {'object': ob_master, 'detail': True})
        else:
            print "error"
@login_required()
def master_edit(request, master_id=None):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            data = dict()
            if master_id is None:
                form = MasterForm()
                data.update({'form': form})
            else:
                master = Master.objects.get(id=master_id)
                form = MasterForm(initial={'name': master.name,
                                           'id': master.id})
                data.update({'object': master, 'form': form})
            return render(request, 'master/master_form.html', data)
        elif request.method == 'POST':
            form = MasterForm(request.POST)
            if form.is_valid():

                if form.cleaned_data.get('id'):
                    # EDIT
                    master_obj = Master.objects.get(id=form.cleaned_data['id'])
                    master_obj.name = form.cleaned_data['name']
                    master_obj.save()
                else:
                    # CREATE
                    master_obj = Master.objects.create(name=form.cleaned_data['name']                                                   )
                return render(request, 'master/master_detail.html', {'object': master_obj, 'detail': True, 'id':object.id})
            else:
                # ENVIAR MENSAJE
                pass
        else:
            # ENVIAR MENSAJE DE REQUEST ERRONEO
            pass

@login_required()
def master_delete(request, master_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            master_obj = Master.objects.get(id=master_id)
            return render(request, 'master/master_confirm_delete.html', {'object': master_obj, 'detail': True})
        elif request.method == 'POST':
            master_obj = Master.objects.get(id=master_id)
            if not master_obj is None:
                master_obj.delete()

            lista = list_masters()
            return render(request, 'course/course_list.html', {'object_list':lista})

@login_required()
def master_carpeta(request, student_code=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            form = MaterCarpetaForm()
            return render(request, 'master/master_dash_form.html', {'form': form})
        if request.method == 'POST':
            print("entro")
            form = MaterCarpetaForm(request.POST)
            if form.is_valid():
                codigo = int(form.cleaned_data['codigo'])
                estudiante = dar_estudiante_codigo(codigo)

                if estudiante != None:
                    #Maestria del estudiante
                    maestria = dar_maestria_de_estudiante(codigo)
                    #Estado del curso
                    structure = structure_master_courses(codigo)
                    credits = calculate_credits(codigo)
                    list_courses = list_courses_scheme(codigo)
                    list_subject = list_subject_approved(codigo)
                    ingles = ingles_aprobado(estudiante.id)
                    if (ingles == False or ingles == None):
                        ingles = None
                    else:
                        ingles = ingles.to_dict()
                        ingles["grade"]=round(float(ingles["grade"]),2)
                    if list_courses != None:
                        list_courses=list_courses.to_dict()
                    return render(request, 'master/master_dash.html', {'estado': True,
                                                                       'credits': credits,
                                                                       'list_courses': list_courses,
                                                                       'list_subject': list_subject,
                                                                       'obj_estudiante': estudiante,
                                                                       'maestria': maestria,
                                                                       'structure': structure,
                                                                       'form': form,
                                                                       'ingles': ingles
                                                                       })
                else:
                    return render(request, 'master/master_dash.html', {'estado':False,
                                                                       'codigo':codigo,
                                                                       'form':form
                                                                       })

@login_required()
def master_candidatos(request, master_id=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            if  master_id != None:
                obj_estudiantes_lista= dar_estudiantes_proyecto_grado(master_id)
            else:
                obj_estudiantes_lista= dar_estudiantes_proyecto_grado(1)
            master_obj = Master.objects.get(id=master_id)
            return render(request, 'master/master_dash_candidatos.html', {'obj_lista': obj_estudiantes_lista,
                                                                          'maestria_obj':master_obj})


@login_required()
def master_student_course(request, student_code=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            form = MaterStudentCourseForm()
            return render(request, 'master/master_student_course_form.html', {'form': form})
        if request.method == 'POST':
            form = MaterStudentCourseForm(request.POST)
            if form.is_valid():

                codigo = int(form.cleaned_data['codigo'])
                curso = form.cleaned_data['curso']
                #Maestria del estudiante
                maestria = dar_maestria_de_estudiante(codigo)
                estudiante = dar_estudiante_codigo(codigo)

                if estudiante != None:
                    curso_obj = tiene_cruso(estudiante.id, curso)
                    if curso_obj == False:
                        return render(request, 'master/master_dash_curso.html', {'estado': False,
                                                                                 'maestria': maestria,
                                                                                 'obj_estudiante': estudiante,
                                                                                 'codigo':curso
                                                                                 })
                    if curso_obj != None:
                        curso_obj.grade = round(float(curso_obj.grade), 2)
                        return render(request, 'master/master_dash_curso.html', {
                                                                            'estado': True,
                                                                            'maestria': maestria,
                                                                            'obj_estudiante': estudiante,
                                                                            'obj_curso': curso_obj.to_dict(),
                                                                            'credits': credits})
                else:
                        return render(request, 'master/master_dash_curso.html', {'estado': False,
                                                                                     'obj_estudiante': estudiante,
                                                                                     'codigo':curso
                                                                                     })

@login_required()
def master_dar_estudiantes(request, student_code=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            form = darStudentMasterForm()
            return render(request, 'master/master_estudiantes_form.html', {'form': form})
        if request.method == 'POST':
            form = darStudentMasterForm(request.POST)
            if form.is_valid():

                maestria_seleccion = form.cleaned_data['maestria']
                print(maestria_seleccion)
                #Maestria del estudiante
                maestria = dar_maestria_nombre(maestria_seleccion)
                estudiantes_lista = maestria.student_set.all()
                lista = list()
                for obj_course in estudiantes_lista:
                    lista.append(obj_course.to_dict())
                return render(request, 'student/student_list.html', {'object_list': lista})
