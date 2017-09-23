from django.db import models

# Create your models here.
from django.utils import timezone


class UserContact(models.Model):
    author = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(
        default=timezone.now)
    updated_at = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.author.username


class ContactReply(models.Model):
    author = models.ForeignKey('auth.User')
    user_contact = models.ForeignKey(UserContact, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        default=timezone.now)