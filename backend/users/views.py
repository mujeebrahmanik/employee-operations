from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class LoginView(APIView):

    def post(self,request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        response = Response(
            {
                'user' : data['user'],
            },
                status= status.HTTP_200_OK
        )

        response.set_cookie(
            key="access_token",
            value=data['access'],
            httponly=True,
            secure=True,
            samesite='Lax',
            max_age=30*60
        )

        response.set_cookie(
            key="refresh_token",
            value=data['refresh'],
            httponly=True,
            secure=True,
            samesite='Lax',
            max_age=7 * 24 * 60 * 60,
        )

        return response



        

