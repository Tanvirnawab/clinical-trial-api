from django.urls import path
from .views import ClinicalTrialListCreateView, ClinicalTrialDetailView

urlpatterns = [
    path('', ClinicalTrialListCreateView.as_view(), name='trial-list-create'),
    path('<int:pk>/', ClinicalTrialDetailView.as_view(), name='trial-detail'),
]
