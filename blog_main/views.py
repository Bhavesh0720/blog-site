from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog


def home(request):
    fp = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    con = {
        'fp':fp,
        'posts':posts,
    }
    return render(request, 'home.html', con)


