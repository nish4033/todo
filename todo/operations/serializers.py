from rest_framework import serializers

from todo.operations.models import Task
from todo.utils.custom_exception import PermissionDenied


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "user", "created", "status")

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task

    def update(self, instance, validated_data):
        try:
            instance = Task.objects.get(pk=instance)
        except Task.DoesNotExist:
            # Handle the case where the specified primary key does not exist
            raise serializers.ValidationError({"details": "no such task exist"})
        if validated_data["user"] != instance.user:
            raise PermissionDenied(
                {"details": "you are not allowed to do this operation"}
            )
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance


class TodoDetailsSerializer(serializers.Serializer):
    STATUS_CHOICE = [
        ("P", "Pending"),
        ("C", "Completed"),
    ]
    title = serializers.CharField(max_length=200, required=False)
    status = serializers.ChoiceField(choices=STATUS_CHOICE, required=False)
    description = serializers.CharField(max_length=249, required=False)
    created = serializers.DateTimeField(required=False)
