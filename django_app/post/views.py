from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'post/post_list.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        post.delete()
    return redirect('post:post_list')


def post_modify(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['photo']
            comment = request.POST['comment']
            post.photo = image
            post.comment = comment
            post.save()

        return redirect('post:post_list')

    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'post/post_modify.html', context)
