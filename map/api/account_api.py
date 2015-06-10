
from django.views.decorators.csrf import csrf_exempt
from proxy_server.decorators import expose_service
from mati.utils import validate_data
from django.http import HttpResponse
from django.contrib import auth

@csrf_exempt
@expose_service(['POST'], public=True)
def account(request, account_id=None):

    if request.method == 'POST':
        print "hi"
        print "Kelvin guerrero"
        return HttpResponse(unicode('Prueba'), status=500)
    #return HttpResponse({"logeado":"hi"}, status=200, content_type='application/json')
    # if request.method == 'PUT':
    #     data = request.POST
    #     #third_party_token = request.GET.get('access_token')
    #     user = request.backend.do_auth(username=data["token"])
    #     json_obj = {"logeado":user}
        # if user:
        # login(request, user)
        # if validate_data(data, attrs=['user', 'pass']):
        #     user = auth.authenticate(username=data["user"], password=data["pass"])
        #     json_obj = {"logeado":user}
        #     return HttpResponse(json_obj, status=200, content_type='application/json')
        # else:
        #     return HttpResponse(status=500)
