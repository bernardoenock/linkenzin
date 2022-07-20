from django.shortcuts import get_object_or_404
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from accounts import permissions
from accounts.models import Account

from .serializers import EducationSerializer, Education

class ListCreateEducationsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwnerAccountOnly]
    
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_queryset(self):
        account = get_object_or_404(Account, pk=self.request.user.id)
        queryset = Education.objects.filter(account=account)
        return queryset

    def perform_create(self, serializer):
        return serializer.save(account=self.request.user)

class RUDEducationsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwnerAccountOnly]
    
    queryset = Education.objects.all()
    serializer_class = EducationSerializer




