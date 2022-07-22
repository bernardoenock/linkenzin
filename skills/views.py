# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

# from .filters import SkillTextFilter
from .models import Skill
from .serializers import SkillSerializer
# from .permissions import IsAdminOrReadOnly


class ListCreateSkillView(generics.ListCreateAPIView):
    # permission_classes = [IsAdminOrReadOnly]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class RetrieveUpdateDestroySkillView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminOrReadOnly]

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SearchSkillView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = SkillTextFilter
