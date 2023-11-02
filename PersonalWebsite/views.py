from django.shortcuts import render
from personal_info_app.models import Personalinfo
from clients_app.models import Client

def main (request):
    personal_info = Personalinfo.objects.all().last()
    clients = Client.objects.all()
    return render(request,'index.html', context={'personal_info' : personal_info,'clients' : clients})
