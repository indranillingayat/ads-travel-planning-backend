from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer
from utils.views.viewset import AppViewProvider


# Create your views here.
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '@')
        password = request.data.get('password', '')
        username = email.split('@')[0]
        serializer = self.get_serializer(data={'username': username, 'password': password})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserViewSet(AppViewProvider, ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['get'], detail=False)
    def current_user(self, request):
        current_user = request.user
        return Response(UserSerializer(current_user).data)
