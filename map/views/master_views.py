from map.models import Master
from django.shortcuts import render
from map.common.master_common import list_masters
from map.forms import MasterForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


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
                return render(request, 'master/master_detail.html', {'object': master_obj, 'detail': True})
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