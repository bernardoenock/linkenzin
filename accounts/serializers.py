from django.forms import CharField, EmailField
from rest_framework import serializers


# Serializer de relações
from addresses.serializers import AddressAccountSerializer, AddressSTRSerializer
from educations.serializers import EducationSerializer

# Models
from .models import Account


class RegisterAccountSerializer(serializers.ModelSerializer):
    address = AddressAccountSerializer(read_only=True)
    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "cpf",
            "phone",
            "gender", 
            "type_account",     
            "is_staff_company",
            "create_at", 
            "update_at", 
            "address"
        ]
        read_only_fields = ["id", "create_at", "update_at"]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_date: dict) -> Account:

        account = Account.objects.create_user(**validated_date)

        typee = account.type_account
        if typee == "Admin":
            Account.delete(account)
            raise serializers.ValidationError({
                "type_account": [
		            "This field is required."
	            ]})

        if typee == "Leader" or typee == "Recruiter" or typee == "Hired":
            Account.delete(account)
            validated_date['is_staff_company'] = True
            account = Account.objects.create_user(**validated_date)

        return account

class ListAccountSerializer(serializers.ModelSerializer):
    address = AddressSTRSerializer(read_only=True)
    educations = EducationSerializer(many=True, read_only=True)


    class Meta:
        model = Account
        fields = "__all__"


    def to_representation(self, instance):
        typee = instance.type_account
        if typee == "Admin":
            return {
                'id': instance.id,
                'is_superuser': instance.is_superuser,
                'first_name': instance.first_name
            }
        elif typee == "Candidate":
           
            return {
                'id': instance.id,
                'first_name': instance.first_name
            }
        elif typee == "Hired":
           
            return {
                'id': instance.id,
                'first_name': instance.first_name
            }
        elif typee == "Leader":
           
            return {
                'id': instance.id,
                'first_name': instance.first_name
            }
        elif typee == "Recruiter":
           
            return {
                'id': instance.id,
                'first_name': instance.first_name
            }


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)



    