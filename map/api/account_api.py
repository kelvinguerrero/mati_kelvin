from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from django.contrib import auth
import json

@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def account(request):

    if request.method == 'POST':
        data = request.POST
        if validate_data(data, attrs=['user', 'pass']):
            user = auth.authenticate(username=data["user"], password=data["pass"])
            auth.login(request, user)
            return HttpResponse({"logeado"}, status=200, content_type='application/json')
        else:
            return HttpResponse(status=500)
