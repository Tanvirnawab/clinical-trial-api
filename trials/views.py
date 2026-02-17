from rest_framework import generics, permissions
from .models import ClinicalTrial
from .serializers import ClinicalTrialSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ClinicalTrialListCreateView(generics.ListCreateAPIView):
    queryset = ClinicalTrial.objects.all().order_by("-created_at")
    serializer_class = ClinicalTrialSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # Filtering
    filterset_fields = ['status']

    # Search
    search_fields = ['title', 'condition']

    # Ordering
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']  # default ordering

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ClinicalTrialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClinicalTrial.objects.all().order_by("-created_at")
    serializer_class = ClinicalTrialSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
