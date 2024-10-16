from rest_framework import serializers

class AddSerializer(serializers.Serializer):
    number1 = serializers.FloatField()
    number2 = serializers.FloatField()
    