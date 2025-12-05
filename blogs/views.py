from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):
    #fetch the posts belongs to the category
    posts = Blog.objects.filter(status='Published', category_id=category_id)
    # return HttpResponse(posts)
    
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    context = {
        'posts':posts,
        'category':category,
    }

    return render(request, 'posts_by_category.html', context)