from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    Choices = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts_related')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=Choices, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    object = models.Manager
    Aba = PublishedManager()

    def get_obsolute_url(self):
        return reverse('blogsite_app : post_detail',
                       args=[self.publish.year, self.publish.month, self.publish.day, self.slug])