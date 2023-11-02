from django.shortcuts import render
from personal_info_app.models import Personalinfo
from contact_app.models import Contact

def contact(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        text = request.POST.get('text')
        Contact.objects.create(fullname=fullname,email=email,text=text)
    personal_info = Personalinfo.objects.all().last()

    return render(request,'contact.html', context={'personal_info' : personal_info})
