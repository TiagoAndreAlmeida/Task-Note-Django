from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from api_v1.serializers import TaskSerializer
from rest_framework.response import Response

from task_app.models import Task

class TaskView(viewsets.ViewSet):
    
    def list(self, request, *args, **kwargs):
        _owner = request.GET.get("owner", "")
        if _owner != "":
            queryset = Task.objects.filter(owner=_owner)
            serializer = TaskSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "owner params must be send"}, status=status.HTTP_400_BAD_REQUEST)
        

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        #on url request must set / on last
        #www..../tasks/15/
        instance = Task.objects.get(id=pk)
        serializer = TaskSerializer(
            instance=instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = Task.objects.get(id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)