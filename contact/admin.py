from django.contrib import admin

# Register your models here.
from .models import UserContact, ContactReply

admin.site.register(UserContact)
admin.site.register(ContactReply)