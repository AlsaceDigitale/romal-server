from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import User
from users.serializers import UserSerializer, UserWithTokenSerializer

class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def login(self, request, pk=None):
        login = request.data.get('login', None)
        if login is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get_or_create(username=login)[0]
        serializer = UserWithTokenSerializer(user)
        return Response(serializer.data)
