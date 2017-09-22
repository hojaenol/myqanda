from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, renderers, permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


from notice.models import Notice
from notice.paginations import NoticePagination
from notice.serializers import NoticeListSerializer, NoticeRetrieveSerializer


class NoticeViewSet(viewsets.GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Notice.objects.all()
    pagination_class = NoticePagination

    def get_serializer_class(self):
        try:
            self.request.parser_context['kwargs']['pk']
            return NoticeRetrieveSerializer
        except KeyError:
            return NoticeListSerializer

    # def list(self, request, *args, **kwargs):
    #     self.serializer_class = NoticeListSerializer
    #     return super(NoticeViewSet, self).list(request, *args, **kwargs)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     self.serializer_class = NoticeRetrieveSerializer
    #     return super(NoticeViewSet, self).retrieve(request, *args, **kwargs)


    def get_permissions(self):
        return (permissions.IsAuthenticated(),)
