from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models


class QandaUser(User):
    created_at = models.DateTimeField(auto_now_add=True)