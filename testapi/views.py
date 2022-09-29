from rest_framework.viewsets import ModelViewSet

from testapi.models import TestModel1
from testapi.serializers import TestModel1Serializer
from utils.views.viewset import AppViewProvider


class TestModel1ViewSet(AppViewProvider, ModelViewSet):
    serializer_class = TestModel1Serializer
    queryset = TestModel1.objects.all()
