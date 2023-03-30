from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from oAuth.models import NewUser
from django.db.models import Q
from demo_admin_api.settings import FRONTEND_URL
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
    http_method_names = ['get', 'post']
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_info = self.perform_create(serializer)
        user_info.is_active = False
        user_info.set_password(request.data["password"])
        user_info.save()
        code = user_info.code
        # url = request.build_absolute_uri(f"/api/user_activate/{code}")
        url = f"{FRONTEND_URL}/#/activate?code={code}"
        print(url)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET')

    def retrieve(self, request, *args, **kwargs):
        instance = NewUser.objects.get(code=kwargs['pk'])
        instance.is_active = True
        instance.save()
        data = {
            "status": "success",
        }
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        return Response(data, status.HTTP_200_OK)

