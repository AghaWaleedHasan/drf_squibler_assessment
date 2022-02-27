from django.shortcuts import render
from .serializers import SectionSerializer, SectionCreateSerializer
from .models import Section
from rest_framework import viewsets
from .mixins import GetSerializerClassMixin
# Create your views here.

class SectionViewset(GetSerializerClassMixin, viewsets.ModelViewSet):
    model = Section
    serializer_class = SectionSerializer
    lookup_field = 'slug'
    serializer_action_classes = {
        'create' : SectionCreateSerializer,
        'update' : SectionCreateSerializer
    }
    
    def get_queryset(self):
        if self.action == 'list':
            return(Section.objects.filter(user=self.request.user,parent__isnull=True))
        return(Section.objects.filter(user=self.request.user))