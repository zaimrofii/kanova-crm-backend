from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ClientStatusViewSet, InteractionNoteViewSet, ReminderViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('statuses', ClientStatusViewSet)
router.register('notes', InteractionNoteViewSet, basename='notes')
router.register('reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
