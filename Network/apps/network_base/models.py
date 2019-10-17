from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)


class Post(models.Model):
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.user}, {self.content}, {self.likes}"

    def __str__(self):
        return f"{self.user}, {self.content}, {self.likes}"

