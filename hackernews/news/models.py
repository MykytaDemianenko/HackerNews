from django.db import models
from authentication.models import User


class New(models.Model):
    title = models.CharField(max_length=55)
    link = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    class Meta:
        db_table = "news"


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='commentator', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(New, related_name='news', on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"


class Upvote(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    new = models.ForeignKey(New, related_name='new', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "upvotes"
