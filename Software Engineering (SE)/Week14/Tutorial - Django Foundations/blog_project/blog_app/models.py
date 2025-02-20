# blog_app\models.py

from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)


    # Below we want to create a display and this will be helpful when we
    # look at the data in the admin page
    def __str__(self):
        return self.title
