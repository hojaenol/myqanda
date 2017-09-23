from django.db import models

# Create your models here.
from django.utils import timezone

from account.models import User


class UserContact(models.Model):
    author = models.OneToOneField(User, related_name="contact")
    created_at = models.DateTimeField(
        default=timezone.now)
    updated_at = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.author.username


class ContactReply(models.Model):
    author = models.ForeignKey(User, related_name="contact_replies")
    user_contact = models.ForeignKey(UserContact, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        default=timezone.now)