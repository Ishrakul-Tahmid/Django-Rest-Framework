from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProjectFilter
from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = ProjectFilter  # Use our custom filter
