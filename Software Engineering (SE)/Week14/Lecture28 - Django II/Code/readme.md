## **Step 1: Install Python and Virtual Environment**
Ensure Python is installed:

```bash
python --version
```

If `virtualenv` is not installed, install it:

```bash
pip install virtualenv
```

---

## **Step 2: Create and Activate a Virtual Environment**
Navigate to the directory where you want your project and create a virtual environment:

```bash
python -m venv myenv
```

Activate the virtual environment:

- **Windows:**
  ```bash
  myenv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source myenv/bin/activate
  ```

---

## **Step 3: Install Django**
Inside the virtual environment, install Django:

```bash
pip install django
```

Verify installation:

```bash
django-admin --version
```

---

## **Step 4: Create the Django Project**
Create the **book_store** project:

```bash
django-admin startproject book_store
```

Navigate into the project directory:

```bash
cd book_store
```

---

## **Step 5: Run Migrations**
Before creating a superuser, apply initial migrations:

```bash
python manage.py migrate
```

---

## **Step 6: Create a Superuser**
Create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- **Username** (e.g., `admin`)
- **Email Address** (optional)
- **Password** (enter and confirm a secure password)

If successful, you'll see:

```
Superuser created successfully.
```

---

## **Step 7: Run the Development Server**
Start the Django server:

```bash
python manage.py runserver
```

Visit:  
```
http://127.0.0.1:8000/admin/
```
Log in using the **superuser credentials**.

✅ Now, we have the admin panel set up and ready!

---

## **Step 8: Create the Books App**
Django projects consist of apps. Create an app named **books**:

```bash
python manage.py startapp books
```

---

## **Step 9: Register the App in Django**
Open `book_store/settings.py` and add `'books'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',  # Add this line
]
```

---

## **Step 10: Create a "Hello World" View**
Open `books/views.py` and define a simple view:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

---

## **Step 11: Configure URLs**
Edit `book_store/urls.py` to include the new app’s URL:

```python
from django.contrib import admin
from django.urls import path
from books.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Add this line
]
```

Restart the server and visit `http://127.0.0.1:8000/`. You should see:

```
Hello, Django!
```

---

## **Step 12: Create the Book Model**
In `books/models.py`, define the **Book** model:

```python
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

---

## **Step 13: Register the Model in the Admin Panel**
To manage books via the Django admin, edit `books/admin.py`:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
```

Now, books will be visible in the admin panel.

---

## **Step 14: Run Migrations**
Apply the database changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **Step 15: Create a Simple Book Form**
In `books/forms.py`, create a Django form with validation:

```python
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Book name must be at least 3 characters long.")
        return name
```

---

## **Step 16: Create a View for Adding Books**
In `books/views.py`, add a view to handle book submissions:

```python
from django.shortcuts import render, redirect
from .forms import BookForm

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
```

---

## **Step 17: Configure URLs for the Book Form**
Create `books/urls.py`:

```python
from django.urls import path
from .views import add_book, book_success

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('success/', book_success, name='book_success'),
]
```

Update `book_store/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]
```

---

## **Step 18: Create the HTML Template**
Create a `templates` folder inside the `books` app:

```bash
mkdir books/templates
mkdir books/templates/books
```

Create `books/templates/books/add_book.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Add a Book</title>
</head>
<body>
    <h1>Add a New Book</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Add Book</button>
    </form>
</body>
</html>
```

---

## **Step 19: Run the Server and Test**
Restart the server:

```bash
python manage.py runserver
```

✅ **Visit Django Admin Panel**:  
Go to `http://127.0.0.1:8000/admin/`  
Log in with the **superuser credentials** to **view and manage books**.

✅ **Visit Book Form**:  
Go to `http://127.0.0.1:8000/books/add/`  
Enter book details and submit. If successful, you'll be redirected to a success page.

---

### 🎉 **Congratulations!**
You now have:
✅ **Django admin panel with a superuser**  
✅ **Book model registered in admin**  
✅ **A form with validation for adding books**  
✅ **A complete Django project setup**  