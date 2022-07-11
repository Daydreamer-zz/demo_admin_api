from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from oAuth.models import NewUser
from oAuth.serializers import NewUserSerializer


# Create your views here.ListAPIView
class UserInfoViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        user = request.user
        serializer = NewUserSerializer(user)
        return Response({"msg": "success", "data": serializer.data})


