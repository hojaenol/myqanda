from rest_auth import serializers


class LoginSerializer(serializers.LoginSerializer):
    pass


from rest_auth.registration import serializers

class RegisterSerializer(serializers.RegisterSerializer):
    pass