from django import forms
from .models import Post, Comment, Review

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'published']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']