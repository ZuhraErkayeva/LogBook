from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from django.utils import timezone

from django.db import models

class Posts(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='date')
    author_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description1 = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.date.year, self.date.month, self.date.day, self.slug])



class PostImage(models.Model):
    post = models.ForeignKey(Posts, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"  # More informative string representation

class Contact(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Privacy_policy(models.Model):  # Class name convention (CamelCase)
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title

class Terms_condition(models.Model):  # Class name convention (CamelCase)
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
