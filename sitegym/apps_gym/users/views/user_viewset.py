from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models.user import User
from ..serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["role"]  # фильтр по ролям (?role=trainer)
    search_fields = ["email", "first_name", "last_name", "middle_name"]
    ordering_fields = ["id", "last_name", "first_name", "email"]
    ordering = ["last_name", "first_name"]

    def get_queryset(self):
        # Селективный выбор полей для оптимизации
        return User.objects.only("id", "email", "first_name", "last_name", "middle_name", "role")
