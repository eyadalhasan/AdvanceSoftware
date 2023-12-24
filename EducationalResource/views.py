from django.shortcuts import render
from rest_framework import viewsets
from EducationalResource.models import EducationalResource
from EducationalResource.serializers import EducationalResourceSerializer

class EducationalResourceViewSet(viewsets.ModelViewSet):
    queryset = EducationalResource.objects.all()
    serializer_class = EducationalResourceSerializer