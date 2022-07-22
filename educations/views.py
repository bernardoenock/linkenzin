from django.shortcuts import get_object_or_404
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from accounts import permissions
from accounts.models import Account

from .serializers import EducationSerializer, Education

class ListCreateEducationsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwnerAccountOnly]
    
    serializer_class = EducationSerializer

    def get_queryset(self):
        self.account = get_object_or_404(Account, id=self.request.user.id)

        queryset = Education.objects.filter(account=self.account)
        
        
        return queryset

    def perform_create(self, serializer: EducationSerializer):
        account = get_object_or_404(Account, id=self.request.user.id)
        
        

        serializer.is_valid(raise_exception=True)
        serializer.save(account=account)

class RUDEducationsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsOwnerAccountOnly]
    
    queryset = Education.objects.all()
    serializer_class = EducationSerializer




