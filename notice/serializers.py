from rest_framework import serializers

from notice.models import Notice


class NoticeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id',
                  'title',
                  )

class NoticeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = NoticeListSerializer.Meta.fields + (
            'created_at',
            'text',
        )


