from rest_framework.viewsets import ModelViewSet
from .models import UserMobil
from .serializers import UserMobilModelSerializer


class UserMobilModelViewSet(ModelViewSet):
    queryset = UserMobil.objects.all()
    serializer_class = UserMobilModelSerializer
