from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import BlogForm, PostForm
from .models import Blog, Post


def check_blog_owner(blog, request):
    """Verify ownership of a blog."""
    if blog.owner != request.user:
        return render(
            request,
            'blogs/no_permission.html',
            status=403
        )
    return None


def index(request):
    posts = Post.objects.order_by('-date_added')

    context = {'posts': posts}

    return render(
        request,
        'blogs/index.html',
        context
    )


def blogs(request):
    blogs = Blog.objects.order_by('title')

    context = {'blogs': blogs}

    return render(
        request,
        'blogs/blogs.html',
        context
    )


@login_required
def new_blog(request):

    if request.method != 'POST':
        form = BlogForm()

    else:
        form = BlogForm(data=request.POST)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()

            return redirect('blogs:blogs')

    context = {'form': form}

    return render(
        request,
        'blogs/new_blog.html',
        context
    )


@login_required
def new_post(request, blog_id):

    blog = get_object_or_404(
        Blog,
        id=blog_id
    )

    result = check_blog_owner(blog, request)
    if result:
        return result

    if request.method != 'POST':
        form = PostForm()

    else:
        form = PostForm(data=request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()

            return redirect('blogs:index')

    context = {
        'blog': blog,
        'form': form,
    }

    return render(
        request,
        'blogs/new_post.html',
        context
    )


@login_required
def edit_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    blog = post.blog

    result = check_blog_owner(blog, request)
    if result:
        return result

    if request.method != 'POST':
        form = PostForm(instance=post)

    else:
        form = PostForm(
            instance=post,
            data=request.POST
        )

        if form.is_valid():
            form.save()

            return redirect('blogs:index')

    context = {
        'post': post,
        'form': form,
    }

    return render(
        request,
        'blogs/edit_post.html',
        context
    )
def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('-date_added')

    context = {
        'blog': blog,
        'posts': posts,
    }

    return render(
        request,
        'blogs/blog.html',
        context
    )
def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    posts = blog.post_set.order_by(
        '-date_added'
    )

    context = {
        'blog': blog,
        'posts': posts,
    }

    return render(
        request,
        'blogs/blog.html',
        context
    )

from django.shortcuts import get_object_or_404

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if blog.owner != request.user:
        return render(
            request,
            'blogs/no_permission.html',
            status=403
        )

    blog.delete()

    return redirect('blogs:blogs')