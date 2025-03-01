from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_app/index.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 'blog_app/add_post.html', {'form': form})

@login_required
def view_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_app/view_post.html', {'post': post})

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_post', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_app/edit_post.html', {'form': form, 'post': post})