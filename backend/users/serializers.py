from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        user = authenticate(
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid Username or Password"
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "This account is inactive"
            )

        refresh = RefreshToken.for_user(user)

        return{
            'access':str(refresh.access_token),
            'refresh':str(refresh),
            'user':{
                'id':user.id,
                'username':user.username,
                'email':user.email,
                'role':user.role
            },
        }