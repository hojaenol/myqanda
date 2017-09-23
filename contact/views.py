from rest_framework import viewsets, permissions, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response

from contact.models import UserContact, ContactReply
from contact.serializers import UserContactSerializer, ContactReplySerializer


class UserContactViewSet(viewsets.GenericViewSet, RetrieveModelMixin):
    queryset = ContactReply.objects.all()
    serializer_class = ContactReplySerializer

    def get_permissions(self):
        return (permissions.IsAuthenticated(),)

    def retrieve(self, request, pk=None, **kwargs):
        if pk != 'me':
            return Response(status=status.HTTP_403_FORBIDDEN)
        contact = UserContact.objects.get(author=request.user)
        queryset = self.get_queryset().filter(user_contact=contact)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @list_route(methods=['POST'], serializer_class=UserContactSerializer)
    def get_or_create(self, request):
        contact, _ = UserContact.objects.get_or_create(author=request.user)
        serializer = self.get_serializer(contact)
        return Response(serializer.data)

    @detail_route(methods=['POST'])
    def reply(self, request, pk=None):
        # /api/v1/conatct/me/reply
        if pk != 'me':
            return Response(status=status.HTTP_403_FORBIDDEN)
        contact = UserContact.objects.get(author=request.user)
        data = request.data.copy()
        data['user_contact'] = contact.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

