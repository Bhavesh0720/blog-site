from django.shortcuts import render
from blogs.models import Category, Blog


def home(request):
    categories = Category.objects.all()
    fp = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    con = {
        'categories':categories,
        'fp':fp,
    }
    return render(request, 'home.html', con)