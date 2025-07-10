from rest_framework import viewsets, filters
from .models import Client, ClientStatus, InteractionNote, Reminder
from .serializers import (
    ClientSerializer, ClientStatusSerializer,
    InteractionNoteSerializer, ReminderSerializer
)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('-created_at')
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'phone_number', 'company', 'lifecycle_stage']
    ordering_fields = ['created_at', 'name']


class ClientStatusViewSet(viewsets.ModelViewSet):
    queryset = ClientStatus.objects.all()
    serializer_class = ClientStatusSerializer


class InteractionNoteViewSet(viewsets.ModelViewSet):
    serializer_class = InteractionNoteSerializer

    def get_queryset(self):
        queryset = InteractionNote.objects.all()
        contact_id = self.request.query_params.get('contact')
        type_filter = self.request.query_params.get('type')

        if contact_id:
            queryset = queryset.filter(client_id=contact_id)
        if type_filter and type_filter.lower() != "activity":
            queryset = queryset.filter(type=type_filter)

        return queryset




class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
