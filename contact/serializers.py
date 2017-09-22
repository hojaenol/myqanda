from rest_framework import serializers

from contact.models import ContactReply, UserContact


class UserContactSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserContact
        fields = ('id',
                  'author',
                  'created_at',
                  'updated_at',
                  )


class ContactReplySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ContactReply
        fields = ('id',
                  'author',
                  'user_contact',
                  'content',
                  'created_at',
                  )
