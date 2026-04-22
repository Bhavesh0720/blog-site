from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category

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