from datetime import datetime

from django.db import models


class Article(models.Model):
    article_key = models.CharField(max_length=63)
    title = models.CharField(max_length=511)
    description = models.CharField(max_length=1023)
    image_path = models.CharField(max_length=127, blank=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    category_key = models.CharField(max_length=63)
    creation_date = models.DateTimeField()
    approven = models.IntegerField(default=0)


class Category(models.Model):
    category_key = models.CharField(max_length=63)
    text = models.CharField(max_length=511)
    image_path = models.CharField(max_length=127)


class Comments(models.Model):
    comment_key = models.CharField(max_length=63)
    user_key = models.CharField(max_length=511)
    article_key = models.CharField(max_length=63)
    text = models.CharField(max_length=511)
    creation_date = models.DateTimeField(default=datetime.now())


class User(models.Model):
    user_key = models.CharField(max_length=511, default="")
    login = models.CharField(max_length=511, default="")
    email = models.CharField(max_length=511, default="")
    password = models.CharField(max_length=511, default="")
    token = models.CharField(max_length=511, default="")
    token_expiration = models.DateField()
