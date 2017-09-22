from rest_framework import viewsets, renderers, permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from contact.models import UserContact, ContactReply


class UserContactViewSet(viewsets.GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = UserContact.objects.all()

class ContactReplyViewSet(viewsets.GenericViewSet, RetrieveModelMixin):
    queryset = ContactReply.objects.all()