# courses/urls.property

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses_list, name="courses_list")
]
