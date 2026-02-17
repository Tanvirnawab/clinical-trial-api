from rest_framework import generics, permissions
from .models import ClinicalTrial
from .serializers import ClinicalTrialSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class ClinicalTrialListCreateView(generics.ListCreateAPIView):
    queryset = ClinicalTrial.objects.all()
    serializer_class = ClinicalTrialSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['status']
    search_fields = ['title', 'condition']
    ordering_fields = ['created_at']


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ClinicalTrialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClinicalTrial.objects.all()
    serializer_class = ClinicalTrialSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
