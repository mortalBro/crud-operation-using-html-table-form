from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    summary=serializers.CharField(max_length=500)