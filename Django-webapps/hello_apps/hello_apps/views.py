from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Welcome to Django  Aayush") #db operations if required