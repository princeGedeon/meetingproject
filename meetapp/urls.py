from django.urls import path
from .views import (
    home, all_meetings, add_participant_view, meet_detail_view, transcribe_view,
    generate_summary_view, create_session_view, download_transcription,add_participant
)

urlpatterns = [
path('add_participant/<int:session_id>/', add_participant, name='add_participant'),

    path('', home, name='home'),
    path('meetings/', all_meetings, name='all_meetings'),
    path('meetings/<int:pk>/', meet_detail_view, name='meet_detail_view'),
    path('create-session/', create_session_view, name='create_session'),
    path('transcribe/', transcribe_view, name='transcribe'),
    path('generate_summary/', generate_summary_view, name='generate_summary'),
    path('download/<str:transcription_id>/', download_transcription, name='download_transcription'),


]
