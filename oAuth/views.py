from rest_framework import viewsets, status
from rest_framework.response import Response
from oAuth.models import NewUser
from django.db.models import Q
from oAuth.serializers import UserSerializer


# Create your views here
class UserInfoViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({"msg": "success", "data": serializer.data})


class UserViewSet(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        user = request.user

        # 普通用户不应该看到超管用户
        if user.roles == 1:
            self.queryset = self.queryset.filter(~Q(username="admin"))

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_info = self.perform_create(serializer)
        user_info.is_active = False
        user_info.save()
        code = user_info.code
        print(code)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
