from user.models import User
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.api.serializers import UserListSerializer, UserRegistrationSerializer


class UserListViewSet(ModelViewSet):
    """
    Lista os usuarios da API
    """
    serializer_class = UserListSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        #queryset = User.objects.raw('select * from user_user')
        return queryset

    def list(self, request, *args, **kwargs):
        return super(UserListViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return Response('No Post')

    # GET COM PASSAGEM DE PARAMETRO retorna um usuario especifico http://127.0.0.1:8000/user/2/
    def retrieve(self, request, *args, **kwargs):
        return super(UserListViewSet, self).retrieve(request, *args, **kwargs)

    # PUT
    def update(self, request, *args, **kwargs):
        return super(UserListViewSet, self).update(request, *args, **kwargs)

    # PATCH
    def partial_update(self, request, *args, **kwargs):
        return super(UserListViewSet, self).partial_update(request, *args, **kwargs)


class UserRegistrationAPIView(ModelViewSet):
    serializer_class = UserRegistrationSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        return Response('No method Get')

    def retrieve(self, request, *args, **kwargs):
        return Response('No method Get')

    def create(self, request, *args, **kwargs):
        return super(UserRegistrationAPIView, self).create(request, *args, **kwargs)