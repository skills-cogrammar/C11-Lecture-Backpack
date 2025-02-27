from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from blog_app.models import BlogPost 

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name == "blog_app": 
        # Create or get groups
        readers_group, _ = Group.objects.get_or_create(name='Readers')
        posters_group, _ = Group.objects.get_or_create(name='Posters')

        # Get the content type for BlogPost
        content_type = ContentType.objects.get_for_model(BlogPost)

        # Fetch permissions safely
        try:
            view_permission = Permission.objects.get(codename='view_blogpost', content_type=content_type)
            add_permission = Permission.objects.get(codename='add_blogpost', content_type=content_type)
            change_permission = Permission.objects.get(codename='change_blogpost', content_type=content_type)

            # Assign permissions
            readers_group.permissions.add(view_permission)  # Readers can only view
            posters_group.permissions.add(view_permission, add_permission, change_permission)  # Posters can add & edit

            print("✅ Groups and permissions created successfully!")
        except Permission.DoesNotExist:
            print("❌ Error: Permissions not found. Run 'python manage.py migrate' and try again.")
