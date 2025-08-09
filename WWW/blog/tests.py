from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, Category, Review

class CategoryModelTest(TestCase):
    def test_category_str(self):
        category = Category.objects.create(name="Tech")
        self.assertEqual(str(category), "Tech")

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name="News")

    def test_post_creation(self):
        post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user,
            category=self.category
        )
        self.assertEqual(str(post), "Test Post")
        self.assertEqual(post.author.username, "testuser")

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='commenter', password='12345')
        self.category = Category.objects.create(name="Opinion")
        self.post = Post.objects.create(
            title="Another Post",
            content="Content here.",
            author=self.user,
            category=self.category
        )

    def test_comment_creation(self):
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content="Nice post!"
        )
        self.assertEqual(str(comment), "Nice post!")

class ReviewModelTest(TestCase):
    def test_review_rating(self):
        review = Review.objects.create(rating=4, content="Good read")
        self.assertEqual(review.rating, 4)
