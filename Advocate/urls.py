from django.urls import path, include
from . import views

# responsible for routing

urlpatterns = [
    path('index', views.index, name='index'),
    path('Clientsection', views.Clientsection, name='Clientsection'),
    path('client_list/', views.client_list, name='client_list'),
    path('client_form/', views.client_form, name='client_form'),
    path('case', views.case, name='case'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('clientforms', views.clientforms, name='clientforms'),
    path('personalinfo',views.personalinfo,name='personalinfo'),
    path('Caseinfo',views.Caseinfo,name='Caseinfo')

]
