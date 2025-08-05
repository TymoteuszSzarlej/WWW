from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment, Review
from django.db.models import Count
from django.contrib.auth.decorators import login_required

def blog_index(request):
    categories = Category.objects.all()
    popular_posts = []
    for category in categories:
        post = Post.objects.filter(category=category, published=True).annotate(num_comments=Count('comments')).order_by('-num_comments').first()
        if post:
            popular_posts.append(post)
    latest_posts = Post.objects.filter(published=True).order_by('-created')[:5]
    return render(request, 'blog/index.html', {
        'categories': categories,
        'popular_posts': popular_posts,
        'latest_posts': latest_posts,
    })

def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category, published=True).order_by('-created')
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id, published=True)
    comments = post.comments.filter(approved=True)
    reviews = post.reviews.all()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'reviews': reviews,
    })

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id, published=True)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
            return redirect('post_detail', post_id=post.id)
    return render(request, 'blog/add_comment.html', {'post': post})

@login_required
def add_review(request, post_id):
    post = get_object_or_404(Post, pk=post_id, published=True)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        content = request.POST.get('content', '')
        if rating:
            Review.objects.create(post=post, author=request.user, rating=rating, content=content)
            return redirect('post_detail', post_id=post.id)
    return render(request, 'blog/add_review.html', {'post': post})
