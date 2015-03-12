from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from django.contrib import auth

@expose_service(['GET', 'POST', 'PUT', 'DELETE'], public=True)
def account(request):

    if request.method == 'PUT':
        data = request.POST
        if validate_data(data, attrs=['user', 'pass']):
            user = auth.authenticate(username=data["user"], password=data["pass"])
            json_obj = {"logeado":user}
            return HttpResponse(json_obj, status=200, content_type='application/json')
        else:
            return HttpResponse(status=500)
