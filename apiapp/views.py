from todo.models import Task

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import TaskListSerializer#, TaskDetailSerializer


class TaskListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        qs = Task.objects.filter(done_or_not=True,user=request.user)
        serializer = TaskListSerializer(qs, many=True)
        return Response(serializer.data)


# class TaskDetailApiView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request,pk):
#         try:
#             qs = Task.objects.get(pk=pk,user=request.user)
#         except Task.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = TaskListSerializer(qs)
#         return Response(serializer.data)
#
#     def put(self,request,pk):
#             try:
#                 task = Task.objects.get(pk=pk)
#             except Task.DoesNotExist:
#                 return Response(status=status.HTTP_400_BAD_REQUEST)
#             serializer = TaskListSerializer(task,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#

"""below class can do just like the top classes  """

class TaskRUDApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

