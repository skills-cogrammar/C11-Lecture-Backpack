from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
]