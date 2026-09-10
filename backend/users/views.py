from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from .serializers import *


class LoginView(APIView):
    authentication_classes=[]
    permission_classes=[]

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


class MeView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self,request):
        return Response({
            'id':request.user.id,
            'username':request.user.username,
            'email':request.user.email,
            'role':request.user.role
        })


class RefreshView(APIView):
    authentication_classes=[]
    permission_classes=[]

    def post(self,request):
        refresh_token=request.COOKIES.get("refresh_token")

        if not refresh_token:
            raise AuthenticationFailed("Refresh token not found .")

        serializer = TokenRefreshSerializer(
            data = {"refresh":refresh_token }
        )

        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data

        response = Response(
            {'message':'Access Token refreshed'},
            status=status.HTTP_200_OK
        )

        response.set_cookie(
            key='access_token',
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
            secure=False,
            samesite="Lax",
            max_age=7 * 24 * 60 * 60,
        )

        return response