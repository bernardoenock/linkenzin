from rest_framework import serializers

from .models import Address


class AddressAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        

class AddressSTRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["zip_code", "number", "complement"]