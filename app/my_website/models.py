from django.db import models

class Article(models.Model):
    title = models.TextField()
    Author = models.TextField(default=None, blank=True)