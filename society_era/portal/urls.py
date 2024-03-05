from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.Register, name='register'),
    path("login/",views.Login, name='login'),
    path("logout/",views.Logout, name='logout'),
    path("home/",views.HomePage, name='home'),
    path("community/",views.community, name='community'),
    path('build_community/', views.build_community, name='build_community'),
    path('join_community/',views.join_community, name='join_community'),
    path("references/",views.references, name='references'),
    path("generate/",views.GenerateRefID, name='generate'),
    path("services/",views.services, name='services'),
]
