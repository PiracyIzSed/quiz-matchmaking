from rest_framework import serializers
from player.models import Player,PlayerQueue

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerQueue
        fields = '__all__'
