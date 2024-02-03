from django.urls import path
from . import views

urlpatterns = [
    path("",views.First, name='first'),
    path("register/",views.Register, name='register'),
    path("login/",views.Login, name='login'),
    path("home/",views.HomePage, name='home'),
    path("community/",views.community, name='community'),
    path("references/",views.references, name='references'),
    path("generate/",views.GenerateRefID, name='generate'),
    path("services/",views.services, name='services'),
]