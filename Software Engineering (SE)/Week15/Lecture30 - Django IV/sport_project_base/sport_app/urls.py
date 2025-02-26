# sport_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('protected/', views.protected_view, name='protected'),
]
