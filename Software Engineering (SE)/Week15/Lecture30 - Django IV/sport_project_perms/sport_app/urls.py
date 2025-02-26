# sport_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrants', views.registrants, name='registrants'),
    path('registration/', views.sport_registration, name='sport_registration'),
    path('registrants/delete/<int:id>', views.delete_registration, name='delete_registrant'),
]
