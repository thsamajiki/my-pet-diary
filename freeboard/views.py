from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def index(request):
    post_list = Post.objects.order_by('-pub_date')
    
    context = {
        'post_list': post_list
    }
    
    return render(request, 'freeboard/post_list.html', context)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
    'post': post
    }
    return render(request, 'freeboard/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('freeboard:index')
    else:
        form = PostForm()
        context = {'form': form}
    return render(request, 'freeboard/post_form.html', context)