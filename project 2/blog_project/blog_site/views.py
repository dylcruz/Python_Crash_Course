from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import BlogForm, BlogEntryForm
from .models import Blog, BlogEntry

def index(request):
    return render(request, 'blog_site/index.html')

@login_required()
def blogs(request):
    blogs = Blog.objects.order_by('date_added')
    context = {"blogs": blogs}
    return render(request, "blog_site/blogs.html", context)

@login_required()
def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    entries = blog.blogentry_set.order_by('-date_added')
    context = {"blog": blog, "entries": entries}
    return render(request, "blog_site/blog.html", context)

@login_required()
def create_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST) 
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blog_site:blogs')
    context = {'form': form}
    return render(request, "blog_site/create_blog.html", context)

@login_required()
def create_entry(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(request.user, blog.owner)

    if request.method != 'POST':
        form = BlogEntryForm()
    else:
        form = BlogEntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.blog = blog
            form.save()
            return redirect('blog_site:blog', blog_id=blog_id)
    context = {'form': form, 'blog': blog}
    return render(request, 'blog_site/create_entry.html', context)

@login_required()
def edit_entry(request, entry_id):
    entry = BlogEntry.objects.get(id=entry_id)
    blog = entry.blog
    check_blog_owner(request.user, blog.owner)

    if request.method != 'POST':
        form = BlogEntryForm(instance=entry)
    else:
        form = BlogEntryForm(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('blog_site:blog', blog_id=blog.id)
    context = {"form": form, "entry": entry, "blog": blog}
    return render(request, "blog_site/edit_entry.html", context)

def check_blog_owner(user, blog_owner):
    if user == blog_owner:
        return
    else:
        raise Http404
