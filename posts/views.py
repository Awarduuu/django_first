from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm


@login_required
def create(request):
    # if request.method =="POST":
    #     title = request.POST.get('title')
    #     user = request.user
    #     content = request.POST.get('content')
    #     image = request.FILES.get('image')
    #     Post.objects.create(title=title, content=content, image=image, user=user)
    #     return redirect('posts:main')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user = request.user)
        return redirect('main')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form' : form})


def main(request):
    posts = Post.objects.all()
    return render(request,'posts/main.html', {'posts': posts})


def show(request, id):
    post = Post.objects.get(pk=id)
    post.view_count += 1
    post.save()
    return render(request,'posts/show.html', {'post': post})

def update(request, id):
   
#    if request.method =="POST":
#        post.title = request.POST.get('title')
#        post.content = request.POST.get('content')
#        post.image = request.FILES.get('image')
#        post.save()
#        return redirect('posts:show', post.id)
#    return render(request,'posts/update.html', {"post":post})
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(user = request.user)
            return redirect('post:show', post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update.html', {'form' : form})

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("posts:main")

@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.like_user_set.all():
        post.like_user_set.remove(request.user)
    else:
        post.like_user_set.add(request.user)

    # post_like, post_like_created = post.like_set.get_or_create(user=request.user)
    # if not post_like_created:
    #   post_like.delete()
    if request.GET.get('redirect_to') == 'show':
        return redirect('posts:show', post_id)
    else:   
        return redirect('posts:main')
@login_required

def like_list(request):
    likes = request.user.like_set.all()
    return render(request, 'posts/like_list.html', {'likes':likes})

# Create your views here.
