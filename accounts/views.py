# Generic and Views
from rest_framework import generics
from rest_framework.views import APIView, Response, status


# Authentications
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# Permissions
from . import permissions

# Account
from . import models, serializers

# Address
from addresses.serializers import AddressAccountSerializer
from addresses.models import Address

# POST /api/accounts/register/ 
class RegisterAccountView(generics.CreateAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.RegisterAccountSerializer

    def perform_create(self, serializer):

        if not self.request.data["address"]:
            return serializer.save()

        address_serializer = AddressAccountSerializer(data=self.request.data["address"])
        address_serializer.is_valid(raise_exception=True)
        address = Address.objects.create(**address_serializer.validated_data)
        address.save()
        return serializer.save(address=address)
    
# GET /api/accounts/
class ListAllAccountsView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdmOnly]

    queryset = models.Account.objects.all()
    serializer_class = serializers.ListAccountSerializer

# GET UPDATE DELETE /api/accounts/<int:pk>
class RUDAccountView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwnerOrAdmin]
    
    queryset = models.Account.objects.all()
    serializer_class = serializers.ListAccountSerializer

# POST /api/accounts/login/
class LoginAccountsView(APIView):
       def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"},
            status.HTTP_401_UNAUTHORIZED,
        )