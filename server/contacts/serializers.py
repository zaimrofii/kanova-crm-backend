from rest_framework import serializers
from .models import Client, ClientStatus, InteractionNote, Reminder

class ClientStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientStatus
        fields = '__all__'


class InteractionNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractionNote
        fields = '__all__'


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    notes = InteractionNoteSerializer(many=True, read_only=True)
    reminders = ReminderSerializer(many=True, read_only=True)
    status = serializers.SlugRelatedField(slug_field='id', queryset=ClientStatus.objects.all())

    class Meta:
        model = Client
        fields = '__all__'
