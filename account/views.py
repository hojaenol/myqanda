import json
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserSerializer, LoginSerializer


class UserAPIView(GenericAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


    def post(self, request):
        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None, **kwargs):
        if pk != 'me':
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request):
            user_data = request.data.get('user', {})
            serializer_data = {
                'username': user_data.get('username', request.user.username),
                'email': user_data.get('email', request.user.email),
                'profile': {
                    'bio': user_data.get('bio', request.user.profile.bio),
                    'image': user_data.get('image', request.user.profile.image)
                }
            }
            serializer = self.serializer_class(
                request.user, data=serializer_data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)



class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
