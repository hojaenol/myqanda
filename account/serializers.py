from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'username', 'password',]

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        # validated_data = {'username': '', 'email': '', 'password': ''}
        # **validated_data: username='', email='', password=''
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `User` instance one at a time.
            setattr(instance, key, value)

        if password is not None:
            # `.set_password()`  handles all
            # of the security stuff that we shouldn't be concerned with.
            instance.set_password(password)

        # After everything has been updated we must explicitly save
        # the model. It's worth pointing out that `.set_password()` does not
        # save the model.
        instance.save()

        return instance

class LoginSerializer(serializers.Serializer):
    # LoginSerializer(email='', password='') - __init__ 에 작성
    # LoginSerializer(data=request.data).create(), .save() - def create
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def __init__(self, **kwargs):
        super(LoginSerializer, self).__init__()
        self.key = None
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.user = User.objects.filter(email=self.email).first()
        if self.user:
            authenticate = check_password(self.password, self.user.password)
            if authenticate:
                token, _ = Token.objects.get_or_create(user=self.user)
                self.key = token.key
            else:
                raise Exception("비번 확인해보시죠")

    @property
    def data(self):
        return {'key': self.key}

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass