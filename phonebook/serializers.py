from .models import Contact, Phone
from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    phone_numbers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_numbers']