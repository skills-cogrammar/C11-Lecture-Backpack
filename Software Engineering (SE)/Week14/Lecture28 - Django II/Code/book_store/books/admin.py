from django.contrib import admin
from .models import Book

# Register Book model with custom admin configuration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Configure which fields appear in the list view
    list_display = ('name', 'description', 'created_at')
    # Add search functionality for the 'name' field
    search_fields = ('name',)