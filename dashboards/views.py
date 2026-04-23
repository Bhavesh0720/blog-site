from django.shortcuts import get_object_or_404, render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify
# from django.utils.text import slugify


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.count()
    blog_count = Blog.objects.count()
    con = {
        'category_count':category_count,
        'blog_count':blog_count,
    }
    return render(request, 'dashboard/dashboards.html', con)


def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    con = {
        'form':form,
    }
    return render(request, 'dashboard/add_category.html', con)

@login_required(login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')        
   
    form = CategoryForm(instance=category)
    con = {
        'form':form,
        'category':category,
    }
    return render(request, 'dashboard/edit_category.html', con)

@login_required(login_url='login')
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

@login_required(login_url='login')
def posts(request):
    posts = Blog.objects.all()
    con = {
        'posts':posts,
    }
    return render(request, 'dashboard/posts.html', con)


def generate_slug(title):
    base_slug = slugify(title)
    slug = base_slug 
    counter = 1

    while Blog.objects.filter(slug=slug).exists():
        slug = f'{base_slug}-{counter}'
        counter += 1

    return slug
    
@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporary save so add data like author
            post.author = request.user
            # post.save()            
            post.slug = generate_slug(post.title)
            post.save()
            return redirect('posts')
    form = PostForm()
    con = {
        'form':form,
    }
    return render(request, 'dashboard/add_post.html', con)

@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')