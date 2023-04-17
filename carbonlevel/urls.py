from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('sign_in/', views.sign_in, name='sign_inpage'), 
    path('sign_up/', views.sign_up, name='sign_uppage'),
    path('sign_out/', views.sign_out, name='sign_outpage'),
    path('dashboard/', views.dashboard, name='dashboardpage'),
    path('calculatedresults/', views.calculatedresults, name='calculatedresultspage'),
    #path('add/', views.add, name='add'),

 
]