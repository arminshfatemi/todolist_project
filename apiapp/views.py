from todo.models import Task

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView

from .serializers import TaskSerializer


class TaskListApiView(APIView):
    def get(self,request):
        qs = Task.objects.filter(done_or_not=True,user=request.user)
        serializer = TaskSerializer(qs, many=True)
        return Response(serializer.data)

