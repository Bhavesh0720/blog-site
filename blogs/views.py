from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category, Comment
from django.db.models import Q, Count, Avg

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
    blog_post = get_object_or_404(Blog, slug=slug, status='Published')
    comments = Comment.objects.filter(blog=blog_post).order_by('-created_at')
    total_comments = comments.count()
    avg_rating = comments.aggregate(Avg('rating'))['rating__avg'] or 0
    full_stars = int(avg_rating)
    half_stars = (avg_rating - full_stars)
    empty_stars = 5 - full_stars - (1 if half_stars else 0)
    
    if request.method == 'POST':        
        user = request.user
        blog = get_object_or_404(Blog, slug=slug)
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        Comment.objects.create(            
            user=user,
            blog=blog,
            comment=comment,
            rating=rating
        )
        return HttpResponseRedirect(request.path)

    con = {
        'blog_post':blog_post,
        'comments':comments,
        'total_comments':total_comments,
        'avg_rating':avg_rating,
        'full_stars':range(full_stars),
        'half_stars':half_stars,
        'empty_stars':range(empty_stars),
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


