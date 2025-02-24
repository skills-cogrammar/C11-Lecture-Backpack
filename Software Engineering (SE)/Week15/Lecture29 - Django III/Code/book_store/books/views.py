from django.http import HttpResponse
from .forms import BookForm
from django.shortcuts import render, redirect

def home(request):
    return HttpResponse("Hello, Django!")

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_success')
    else:
        form = BookForm()
    
    return render(request, 'books/add_book.html', {'form': form})

def book_success(request):
    return HttpResponse("Book added successfully!")