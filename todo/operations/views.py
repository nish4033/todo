from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.operations.models import Task
from todo.operations.serializers import TaskSerializer, TodoDetailsSerializer
from todo.utils.custom_exception import PermissionDenied


class TodoAPIView(APIView):
    def post(self, request):
        request.data.update({"user": request.user["user_id"]})
        ser = TaskSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        task = ser.save()
        data = {
            "status": "success",
            "code": 200,
            "message": f"task created successfully. for '{task.title}'",
        }
        return Response(data, status=status.HTTP_201_CREATED)


class TodoDetailsAPIView(APIView):
    def get(self, request):
        user = request.user["user_id"]
        ser = TodoDetailsSerializer(data=request.query_params)
        ser.is_valid(raise_exception=True)
        ser.validated_data.update({"user": user})
        filter_val = ser.validated_data
        tasks = Task.objects.filter(**filter_val)
        serializer = TaskSerializer(tasks, many=True)
        val = serializer.data
        data = {
            "status": "success",
            "code": 200,
            "data": val,
            "message": "Todo item retrieved successfully",
        }
        return Response(data, status=status.HTTP_200_OK)


class TodoUpdateAPIView(APIView):
    def put(self, request, pk):
        user = request.user["user_id"]
        request.data.update({"user": user})
        ser = TaskSerializer(pk, data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        data = {
            "status": "success",
            "code": 200,
            "message": f"task updated successfully. for '{pk}'",
        }
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = request.user["user_id"]
        try:
            todo_item = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            data = {"message": "No such task"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        if user != todo_item.user.id:
            raise PermissionDenied(
                {"details": "you are not allowed to do this operation"}
            )
        todo_item.delete()
        data = {
            "status": "success",
            "code": 200,
            "message": f"task deleted successfully. for '{pk}'",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
