from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, User
from .forms import PostForm

def board(request):
    post_list = Post.objects.order_by('-write_date')

    current_page = int(request.GET.get('page', 1))
    
    paginator = Paginator(post_list, 5)
    last_page = paginator.num_pages
    current_page = min(current_page, last_page)
    start_page = (current_page - 1) // 10 * 10 + 1
    end_page = min(start_page + 9, last_page)

    board = paginator.page(current_page)
    
    context = {
        'post_list': post_list
    }
    
    return render(request, 'freeboard/post_list.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    
    login_session = request.session.get('login_session', '')
    context = {'login_session' : login_session}
    
    # post = get_object_or_404(Post, author_id=post_id)
    # context['freeboard'] = freeboard

    # if post.author.author_id == login_session:
    #     context['author'] = True
    # else:
    #     context['author'] = False
    
    context = {
        'post': post
    }

    return render(request, 'freeboard/post_detail.html', context)


import random, string
def make_random_name():
    random_name = 'user' + str(random.randrange(100, 1000))
    return random_name


# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
def write(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session' : login_session}

    if request.method == 'GET':
        form = PostForm()
        context['forms'] = form
        return render(request, 'freeboard/post_write.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.write_date = timezone.now()

            post.save()
            return redirect('/freeboard')

        else:
            context['forms'] = form
            if form.errors:
                for value in form.errors.values():
                    context['error'] = value
            return render(request, 'freeboard/post_write.html', context)


def modify(request, post_id):
    login_session = request.session.get('login_session', '')
    context = {'login_session' : login_session}

    # post = get_object_or_404(Post, author_id=post_id)

    context = {'post': post}

    # if post.author.id != login_session:
    #     return redirect('../freeboard/post_detail/{post_id}/')

    if request.method == 'GET':
        form = PostForm(instance=post)
        context['forms'] = form
        return render(request, 'freeboard/post_modify.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.subject = form.subject
            post.content = form.content
            post.modify_date = timezone.now()

            post.save()
            return redirect('/freeboard')

        else:
            context['forms'] = form
            if form.errors:
                for value in form.errors.values():
                    context['error'] = value
            return render(request, 'freeboard/post_modify.html', context)


def delete(request, post_id):
    login_session = request.session.get('login_session', '')
    # post = get_object_or_404(Post, author_id=post_id)
    
    # if post.author.author_id != login_session:
    #     return redirect('../freeboard/post_detail/{post_id}/')
    # else:
    #     post.author.author_id == login_session
    #     post.delete()
    #     return redirect('../freeboard')