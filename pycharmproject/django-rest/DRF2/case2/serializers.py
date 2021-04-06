# 此文件用来存放序列化器


# 导入序列化器
from rest_framework import serializers
from . import models

class StudentSer(serializers.Serializer):
    """
    里面写的是每一个需要序列化，反序列
    """
    name = serializers.CharField(label="姓名",max_length=20)
    age = serializers.IntegerField(source="age")
    score = serializers.IntegerField()
