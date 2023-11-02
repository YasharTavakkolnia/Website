from django.shortcuts import render
from personal_info_app.models import Personalinfo
from works_app.models import Work
def work_page(request):
    personal_info = Personalinfo.objects.all().last()
    items = Work.objects.all()
    return render(request, 'works.html',context={'personal_info' :personal_info,'items':items})

def project_detail(request,id):
    personal_info = Personalinfo.objects.all().last()
    project = Work.objects.get(id=id)
    return render(request,'projects.html',context={'project': project,'personal_info' :personal_info})