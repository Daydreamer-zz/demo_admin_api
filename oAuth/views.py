from rest_framework import viewsets
from rest_framework.response import Response
from oAuth.models import NewUser, Books
from oAuth.serializers import NewUserSerializer, BooksSerializer


# Create your views here
class UserInfoViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        user = request.user
        serializer = NewUserSerializer(user)
        return Response({"msg": "success", "data": serializer.data})


class UserViewSet(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
