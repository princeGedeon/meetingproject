from django.urls import path
from .views import (
    home, all_meetings, add_participant_view, meet_detail_view, transcribe_view, check_status_view,generate_summary_view
)

urlpatterns = [
    path('', home, name='home'),
    path('meetings/', all_meetings, name='all_meetings'),
    path('meetings/<int:pk>/', meet_detail_view, name='meet_detail_view'),
    path('participants/add/', add_participant_view, name='add_participant_view'),
    # URLs for transcription and summary generation
    path('votre_vue_django_pour_transcrire/', transcribe_view, name='transcribe'),
    path('votre_vue_django_pour_verifier_statut/', check_status_view, name='check_status'),
    path('votre_vue_django_pour_generer_compte_rendu/', generate_summary_view, name='generate_summary'),

]
