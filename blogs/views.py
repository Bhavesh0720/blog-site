from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category
from django.db.models import Q

# Create your views here.
def post_by_category(request, pk):
    posts = Blog.objects.filter(category=pk, status='Published')
    category = get_object_or_404(Category, pk=pk)

    # try:
    #     category = Category.objects.get(pk=pk)
    # except Category.DoesNotExist:
    #     return redirect('home')      
        
    con = {
        'posts':posts,
        'category':category,
    }
    return render(request, 'post_by_category.html', con)


def blogs(request, slug):
    blog_post = get_object_or_404(Blog, slug=slug)
    con = {
        'blog_post':blog_post,
    }
    return render(request, 'blogs.html', con)


def search(request):
    keyword = request.GET.get('keyword')
    post = Blog.objects.filter(
        (Q(title__icontains=keyword) |
        Q(short_description__icontains=keyword) |
        Q(blog_body__icontains=keyword)), status='Published'
    )
    con = {
        'post':post,
        'keyword':keyword,
    }
    return render(request, 'search.html', con)