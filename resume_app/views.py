from django.shortcuts import render
from personal_info_app.models import Personalinfo
def resume(request):
    personal_info = Personalinfo.objects.all().last()
    return render(request, 'resume.html', context={'personal_info' : personal_info})
