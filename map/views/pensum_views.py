from map.models import Pensum, Master
from django.shortcuts import render
from map.common.pensum_common import list_pensums
from map.forms import PensumForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required()
def pensum(request, pensum_id=None):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            if pensum_id == None:
                lista = list_pensums()
                return render(request, 'pensum/pensum_list.html', {'object_list': lista})
            else:
                ob_pensum = Pensum.objects.get(id=pensum_id)
                return render(request, 'pensum/pensum_detail.html', {'object': ob_pensum, 'detail':True})

@login_required()
def pensum_edit(request, pensum_id=None):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'GET':
        data = dict()
        if pensum_id == None:
            form = PensumForm()
            data.update({'form': form})
        else:
            pensum = Pensum.objects.get(id=pensum_id)
            print(pensum.master.name)
            form = PensumForm(initial={'name': pensum.name, 'active': pensum.active, 'id': pensum.id, 'master':pensum.master.name})
            data.update({'object':pensum, 'form': form})
        return render(request, 'pensum/pensum_form.html', data)
    elif request.method == 'POST':
        form = PensumForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('id'):
                # EDIT
                pensum = Pensum.objects.get(id=form.cleaned_data['id'])
                master_obj = Master.objects.get(name=form.cleaned_data['master'])
                pensum.name = form.cleaned_data['name']
                pensum.active = form.cleaned_data['active']

                print master_obj.name
                pensum.master = master_obj
                pensum.save()
            else:
                # CREATE
                ob_master = Master.objects.get(id=form.cleaned_data['master'])
                pensum = Pensum.objects.create(name=form.cleaned_data['name'], active=form.cleaned_data['active'], master=ob_master.name)
            return render(request, 'pensum/pensum_detail.html', {'object':pensum, 'detail':True})
        else:
            # ENVIAR MENSAJE
            pass
    else:
        # ENVIAR MENSAJE DE REQUEST ERRONEO
        pass

@login_required()
def pensum_delete(request, pensum_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method ==  'GET':
        pensum = Pensum.objects.get(id=pensum_id)
        return render(request, 'pensum/pensum_confirm_delete.html', {'object':pensum, 'detail':True})
    elif request.method == 'POST':
        pensum = Pensum.objects.get(id=pensum_id)
        if not pensum == None:
            pensum.delete()
        lista = list_pensums()
        return render(request, 'pensum/pensum_list.html', {'object_list':lista})