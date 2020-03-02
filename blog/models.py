from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # Status of my post either it is published or it is in draft.
    STATUS_CHOICES = (('draft', 'Draft'),
                      ('published', 'Published'))

    post_id = models.AutoField
    title = models.CharField(max_length=50)
    heading = models.CharField(default="", max_length=50)
    sub_heading = models.CharField(default="", max_length=100)
    body = models.TextField(default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts',default='Devraj')
    publish_date = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=False, default="")
    updated = models.DateTimeField(auto_now=False, default="")
    slug = models.SlugField(max_length=50, unique_for_date=publish_date, default="slug")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title



