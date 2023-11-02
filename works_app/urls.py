from django.urls import path
from . import views
urlpatterns = [
    path('', views.work_page),
    path("<int:id>",views.project_detail,name ="project_detail"),
]