from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'done_or_not', 'created_time', 'updated_time', 'user']
