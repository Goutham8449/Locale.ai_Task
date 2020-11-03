from rest_framework import serializers

from .models import CustomUser, Trip

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
        ]

class TripSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    class Meta:
        model = Trip
        fields = '__all__'