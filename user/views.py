from rest_framework.viewsets import ModelViewSet
from .serializers import (
    User,
    User_serializer
)

class User_view(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serializer

    