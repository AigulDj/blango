from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=30)
  author = models.CharField(max_length=30)
  published_at = models.DateField()
