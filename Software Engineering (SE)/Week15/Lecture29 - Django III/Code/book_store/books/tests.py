from django.test import TestCase
from django.utils import timezone
from .models import Book
from .forms import BookForm

class BookModelTestCase(TestCase):
    def setUp(self):
        Book.objects.create(name="Julien", description="Julien's book")
        Book.objects.create(name="Riaan", description="Riaan's book")
        Book.objects.create(name="Armand", description="Armand's book")

    def test_model_books_count(self):
        count = Book.objects.count()
        self.assertEqual(count, 3)

    def test_model_name_length(self):
        book = Book.objects.create(name="A", description="Short name")
        self.assertLessEqual(len(book.name), 100)

    def test_model_description_length(self):
        book = Book.objects.create(name="Test", description="This is a very long description that should be allowed.")
        self.assertLessEqual(len(book.description), 1000)

    def test_model_created_at(self):
        book = Book.objects.get(name="Julien")
        self.assertIsNotNone(book.created_at)
        self.assertIsInstance(book.created_at, timezone.datetime)

    def test_model_str(self):
        book = Book.objects.get(name="Julien")
        self.assertEqual(str(book), "Julien")

    def test_model_books_title_description(self):
        book1 = Book.objects.get(name="Julien")
        book2 = Book.objects.get(name="Riaan")
        self.assertEqual(book1.description, "Julien's book")
        self.assertEqual(book2.description, "Riaan's book")


class BookFormTestCase(TestCase):
    def test_clean_name_too_short(self):
        # Create a form instance with a name that is too short
        form = BookForm(data={'name': 'ab', 'description': 'Test description'})
        # Check if the 'name' field has the expected error message
        self.assertIn('name', form.errors)
        self.assertEqual(form.errors['name'], ["Book name must be at least 3 characters long."])

    def test_form_save(self):
        form = BookForm(data={'name': 'New Book', 'description': 'New book description'})
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(Book.objects.filter(name='New Book').count(), 1)

    def test_form_short_name(self):
        form = BookForm(data={'name': 'a', 'description': 'New book description'})
        self.assertFalse(form.is_valid())


class BookViewTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, Django!")

    def test_add_book_view(self):
        response = self.client.get('/books/add/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add a New Book")

    def test_add_book_form_submission(self):
        response = self.client.post('/books/add/', {
            'name': 'Test Book',
            'description': 'This is a test book.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(Book.objects.filter(name='Test Book').count(), 1)
