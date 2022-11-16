from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer, UserMinInfoSerializer
from users.utils import get_allowed_user_actions
from utils.views.viewset import AppViewProvider


User = get_user_model()


# Create your views here.
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user = authenticate(username=email, password=password)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserViewSet(AppViewProvider, ModelViewSet):
    serializer_class = UserSerializer
    search_fields = ('first_name', 'last_name', 'username')

    def get_queryset(self):
        return User.objects.none()

    @action(methods=['get'], detail=False)
    def current_user(self, request):
        current_user = request.user
        available_actions = get_allowed_user_actions(request.user)
        res = {
            'user': UserSerializer(current_user).data,
            'actions': available_actions
        }
        return Response(res)

    @action(methods=['get'], detail=False)
    def list_users(self, request, *args, **kwargs):
        return self.custom_list(UserMinInfoSerializer, User.objects.all())
