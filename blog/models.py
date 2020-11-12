from django.contrib import admin
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    class Meta:
        db_table = 'blog'

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    excerpt = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='draft', choices=options)
    author = models.CharField(max_length=500)

    # def __str__(self):
    #     return self.title + ', ' + str(self.published_at) + ', ' + self.status + ', ' + self.author
