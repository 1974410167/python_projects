
from .models import Student,user
from rest_framework import serializers


# 好用
class StudentSer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1  # 指定深度，比如外键，多对多

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'