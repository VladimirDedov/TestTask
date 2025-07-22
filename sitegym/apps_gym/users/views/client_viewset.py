from rest_framework.viewsets import ModelViewSet
from apps_gym.users.models.client_profile import ClientProfile
from apps_gym.users.serializers.client_serializer import ClientProfileSerializer

class ClientProfileViewSet(ModelViewSet):
    queryset = ClientProfile.objects.select_related("user").prefetch_related("trainers")
    serializer_class = ClientProfileSerializer
