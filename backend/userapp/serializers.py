from rest_framework.serializers import HyperlinkedModelSerializer
from .models import UserMobil


class UserMobilModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserMobil
        fields = ['username', 'first_name', 'last_name', 'city', 'email']