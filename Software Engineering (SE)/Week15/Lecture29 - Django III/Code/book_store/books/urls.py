from django.urls import path
from .views import add_book, book_success

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('success/', book_success, name='book_success'),
]