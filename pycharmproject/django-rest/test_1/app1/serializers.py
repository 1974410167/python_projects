from rest_framework.serializers import Serializer
from .models import User




class UserSer(Serializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1



