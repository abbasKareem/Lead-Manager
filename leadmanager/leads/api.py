from .models import Lead
from rest_framework import viewsets, permissions
from .serialiazers import LeadSerializer


class LeadViewSets(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LeadSerializer

