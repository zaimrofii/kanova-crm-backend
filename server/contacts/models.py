import uuid
from django.db import models

class ClientStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    lifecycle_stage = models.CharField(max_length=100, blank=True, null=True)
    status = models.ForeignKey(ClientStatus, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class InteractionNote(models.Model):
    TYPE_CHOICES = [
        ("activity", "Activity"),
        ("note", "Note"),
        ("email", "Email"),
        ("call", "Call"),
        ("task", "Task"),
        ("meeting", "Meeting"),
        ("log", "Log"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="note")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.client.name}"

class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reminders')
    follow_up_date = models.DateField()
    description = models.TextField(blank=True, null=True)
