

from django.urls import path
from . import views
from django.views.generic import TemplateView 


urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    path('base_view/', views.base_view, name='base'), 
    # Portfolio page
    path('folio/', views.portfolio, name='portfolio'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),



    # Custom user management
    path('custom_user/', views.custom_user_list, name='custom_user_list'),  

    # Advocate management
   
    
    path('advocate_view',views.advocate_view,name='advocate_view'),

    

    
    # Teams page with slider
    path('team/', views.team, name='team'),

    path('Client/', views.client_view, name='Client'),
    path('advocate/', views.advocate_view, name='advocate'),
    path('Clerk/', views.clerk_view, name='Clerk'),

    # User registration and login
    
    path('success/', TemplateView.as_view(template_name='success.html'), name='success_page'),  

    # Logout
    path('logout/', views.user_logout, name='user_logout'),
    path('login/',views.login,name='login'),

    path('Advocate_Signup',views.Advocate_Signup,name='Advocate_Signup'),
    path('Advocate_login',views.advocate_login,name='Advocate_login'),
    path('advocate_signin',views.advocate_signin,name='advocate_signin'),
    path('dashboard',views.dashboard,name='dashboard')


    
]
