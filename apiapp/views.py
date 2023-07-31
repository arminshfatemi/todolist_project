from todo.models import Task

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView

from .serializers import TaskListSerializer, TaskDetailSerializer


class TaskListApiView(APIView):
    def get(self,request):
        qs = Task.objects.filter(done_or_not=True,user=request.user)
        serializer = TaskListSerializer(qs, many=True)
        return Response(serializer.data)


class TaskDetailApiView(APIView):
    def get(self,request,pk):
        try:
            qs = Task.objects.get(pk=pk,user=request.user)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskListSerializer(qs)
        return Response(serializer.data)


