from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .serializers import UserSerializer, AgreementSerializer
from butter_exercise.users.models import Agreement


class UserViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class AgreementViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = AgreementSerializer
    queryset = Agreement.objects.all()
    http_method_names = ['get', 'post', 'head', 'delete']
