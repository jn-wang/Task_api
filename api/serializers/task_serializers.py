from api import models
from rest_framework import serializers
# 任务表序列化
class TaskSerializer(serializers.ModelSerializer):
    get_status = serializers.CharField(source='get_get_status_display')
    completion_status = serializers.CharField(source='get_completion_status_display')
    class Meta:
        model = models.Task
        fields = ['id','taskname','publisher','receiver','brokerage','service_fee','create_time','last_time','get_status','completion_status']
        # fields = "__all__"

class TaskDetailSerializer(serializers.ModelSerializer):
    get_status = serializers.CharField(source='get_get_status_display')
    completion_status = serializers.CharField(source='get_completion_status_display')
    class Meta:
        model = models.Task
        fields = ['id', 'taskname', 'publisher', 'receiver', 'brokerage', 'service_fee', 'create_time', 'last_time','get_status', 'completion_status']
