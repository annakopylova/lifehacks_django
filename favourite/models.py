from django.db import models


class ArticleFavourite(models.Model):
    user_id = models.CharField(max_length=511)
    article_id = models.CharField(max_length=511)
    favourite = models.BooleanField()
    like = models.BooleanField()