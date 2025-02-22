"""
From Gower. My Last Question: 
How can you create a Django model with a foreign key relationship, and what happens when the related object is deleted?

*** Example of Foreign Key Relationship
Let’s say you have a Blog model and a Post model. 
Each Post is related to one Blog, so the Post model will have a ForeignKey to the Blog model.
"""

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)  # ForeignKey relationship

    def __str__(self):
        return self.title

"""
The ForeignKey Field
blog = models.ForeignKey(Blog, on_delete=models.CASCADE): This creates the foreign key relationship from Post to Blog.

The on_delete parameter specifies what should happen when the referenced object (the Blog in this case) is deleted.

*** Options for on_delete:
The on_delete parameter controls the behavior when the referenced object (the parent model) is deleted. Here are some common options:

1. -- models.cascade:

blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

If the related object (e.g., Blog) is deleted, all related objects (e.g., Post) will be deleted as well.

Example: If a Blog is deleted, all Post instances associated with that Blog will also be deleted.

2. -- models.PROTECT:

blog = models.ForeignKey(Blog, on_delete=models.PROTECT)

Prevent deletion of the referenced object if there are any related objects 
(i.e., the Post objects cannot be deleted until the Blog is deleted.
So if we block the Blog from being deleted, then the posts are in tact).

3. -- models.SET_NULL:

blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)

Set the foreign key to NULL if the referenced object is deleted. 
This requires the foreign key field to be nullable (null=True).

4. -- models.SET_DEFAULT:

blog = models.ForeignKey(Blog, on_delete=models.SET_DEFAULT, default=1)

Set the foreign key to its default value when the referenced object is deleted. 
You need to define the default value.

5. -- models.SET():

blog = models.ForeignKey(Blog, on_delete=models.SET, default=1)  # Sets to a specific value

Set the foreign key to a specific value or callable when the referenced object is deleted. 
You can pass a function or a constant value.

6. -- models.DO_NOTHING:

blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)

Blog will be deleted if you delete it directly.
Post objects (that have a foreign key to the deleted Blog) will stay intact in the database, 
but they will have a broken reference (the blog_id field will still point to the deleted Blog record, 
which is no longer valid).
"""