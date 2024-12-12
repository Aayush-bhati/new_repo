from rest_framework import serializers
from tasks.models import Tasks,State

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields =(
            'id',
            'title',
            'description'
            )

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields =(
            'id',
            'name'
        )
