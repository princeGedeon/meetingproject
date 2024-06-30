from django.urls import path

from . import views
from .views import meet_detail_view, add_participant_view, all_meetings

urlpatterns = [
    path('', views.home, name='home'),
    path('meet/<int:pk>/', meet_detail_view, name='meet_detail'),
    path('add-participant/', add_participant_view, name='add_participant'),
path('all_meetings/', all_meetings, name='all_meetings'),

]