import os
import uuid

import whisper
from django.contrib.auth.decorators import login_required
from django.contrib.messages.storage import default_storage
from django.core.files.base import ContentFile

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ParticipantForm
from .models import Session
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


def meet_detail_view(request, pk):
    session = get_object_or_404(Session, pk=pk)
    context = {
        'session': session,
    }
    return render(request, 'meets/meetpage.html', context)


def transcribe_audio(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        # Traitement pour transcrire le fichier audio ici
        # Vous pouvez utiliser des services comme AWS Transcribe ou un moteur de transcription personnalisé

        # Exemple simplifié pour la démonstration
        audio_file = request.FILES['audio_file']
        job_name = transcribe_audio_file(audio_file)  # Fonction à implémenter pour la transcription

        return JsonResponse({'job_name': job_name})
    else:
        return JsonResponse({'error': 'Invalid request'})


def generate_summary(request):
    if request.method == 'POST' and 'textToProcess' in request.POST:
        # Traitement pour générer le compte rendu à partir du texte transcrit
        text_to_process = request.POST['textToProcess']

        # Exemple simplifié pour la démonstration
        summary = generate_summary_from_text(text_to_process)  # Fonction à implémenter pour le résumé

        return JsonResponse({'summary': summary})
    else:
        return JsonResponse({'error': 'Invalid request'})


def check_job_status(request):
    if request.method == 'POST' and 'job_name' in request.POST:
        # Vérifier le statut du travail de transcription ici
        job_name = request.POST['job_name']

        # Exemple simplifié pour la démonstration
        status = check_transcription_job_status(job_name)  # Fonction à implémenter pour vérifier le statut

        return JsonResponse({'status': status})
    else:
        return JsonResponse({'error': 'Invalid request'})


# Fonctions à implémenter selon votre logique métier réelle
def transcribe_audio_file(audio_file):
    # Code pour transcrire le fichier audio
    # Cette fonction doit retourner un identifiant de travail (job_name)
    # Utilisez des services tiers ou votre propre infrastructure pour la transcription
    # Exemple : AWS Transcribe, Google Speech-to-Text, etc.
    return "example_job_name"


def generate_summary_from_text(text_to_process):
    # Code pour générer le compte rendu à partir du texte transcrit
    # Cette fonction doit retourner le résumé généré
    # Implémentez votre propre logique de traitement du texte
    return "Example summary text"


def check_transcription_job_status(job_name):
    # Code pour vérifier le statut du travail de transcription
    # Cette fonction doit retourner l'état actuel du travail (en cours, terminé, échec, etc.)
    # Implémentez la logique appropriée selon votre service de transcription
    return "COMPLETED"  # Exemple simplifié

@login_required
def home(request):
    query = request.GET.get('q')
    status = request.GET.get('status')
    sort_by = request.GET.get('sort_by', 'session_debut')

    sessions = Session.objects.all()

    if query:
        sessions = sessions.filter(nom__icontains=query)

    if status:
        sessions = sessions.filter(status=status)

    sessions = sessions.order_by(sort_by)

    latest_session = sessions.last()

    context = {
        'sessions': sessions,
        'latest_session': latest_session,
        'query': query,
        'status': status,
        'sort_by': sort_by,
    }

    return render(request, 'home.html', context)

def all_meetings(request):
    query = request.GET.get('q')
    status = request.GET.get('status')
    sort_by = request.GET.get('sort_by', 'session_debut')

    sessions = Session.objects.all()

    if query:
        sessions = sessions.filter(nom__icontains=query)

    if status:
        sessions = sessions.filter(status=status)

    sessions = sessions.order_by(sort_by)

    context = {
        'sessions': sessions,
        'query': query,
        'status': status,
        'sort_by': sort_by,
    }

    return render(request, 'all_meetings.html', context)

def meet_detail_view(request, pk):
    session = get_object_or_404(Session, pk=pk)
    context = {
        'session': session,
    }
    return render(request, 'meets/meetpage.html', context)

def add_participant_view(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParticipantForm()

    context = {
        'form': form,
    }

    return render(request, 'add_participant.html', context)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def transcribe_view(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']

        # Replace with your Google Cloud credentials and setup
        # Initialize Google Text-to-Speech API client
        # Example: client = google.cloud.speech.SpeechClient()

        # Perform transcription logic using the API client
        # Example: response = client.transcribe(audio_file)

        # Mock response for demonstration
        job_name = "mock-job-123"
        return JsonResponse({'job_name': job_name})

    return JsonResponse({'error': 'POST method with audio_file required'})



@csrf_exempt
def check_status_view(request):
    if request.method == 'POST' and request.POST.get('job_name'):
        job_name = request.POST['job_name']

        # Replace with your Google Cloud credentials and setup
        # Initialize Google Text-to-Speech API client
        # Example: client = google.cloud.speech.SpeechClient()

        # Perform status check logic using the API client
        # Example: status = client.check_status(job_name)

        # Mock response for demonstration
        status = 'COMPLETED'  # Example status

        if status == 'COMPLETED':
            # Fetch transcription result if COMPLETED
            transcription_result = "This is a sample transcription."
            return JsonResponse({'status': status, 'result': transcription_result})
        else:
            return JsonResponse({'status': status})

    return JsonResponse({'error': 'POST method with job_name required'})


@csrf_exempt
def check_status_view(request):
    if request.method == 'POST' and request.POST.get('job_name'):
        job_name = request.POST['job_name']

        # Replace with your Google Cloud credentials and setup
        # Initialize Google Text-to-Speech API client
        # Example: client = google.cloud.speech.SpeechClient()

        # Perform status check logic using the API client
        # Example: status = client.check_status(job_name)

        # Mock response for demonstration
        status = 'COMPLETED'  # Example status

        if status == 'COMPLETED':
            # Fetch transcription result if COMPLETED
            transcription_result = "This is a sample transcription."
            return JsonResponse({'status': status, 'result': transcription_result})
        else:
            return JsonResponse({'status': status})

    return JsonResponse({'error': 'POST method with job_name required'})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def generate_summary_view(request):
    if request.method == 'POST' and request.POST.get('textToProcess'):
        text_to_process = request.POST['textToProcess']

        # Replace with your summary generation logic
        # Example: summary = generate_summary(text_to_process)

        # Mock response for demonstration
        summary = "This is a summary of the meeting."

        return JsonResponse({'summary': summary})

    return JsonResponse({'error': 'POST method with textToProcess required'})

# views.py

from django.shortcuts import render, redirect
from .forms import SessionForm

def create_session_view(request):
    if request.method == 'POST':
        form = SessionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Rediriger vers la page d'accueil après la création
    else:
        form = SessionForm()
    return render(request, 'addmeet.html', {'form': form})



# Vue pour la transcription asynchrone
@csrf_exempt
async def transcribe_view(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']

        try:
            # Sauvegarde du fichier audio téléchargé dans un emplacement temporaire
            file_path = default_storage.save('tmp/' + audio_file.name, ContentFile(audio_file.read()))

            # Chargement du modèle Whisper et transcription de manière asynchrone
            transcription_result, transcription_id = await transcribe_audio(file_path)

            # Suppression du fichier temporaire après la transcription
            os.remove(file_path)

            # Retourne le résultat de la transcription et un identifiant unique
            return JsonResponse({'transcription_id': transcription_id, 'transcription': transcription_result})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'POST method with audio_file required'})

# Fonction pour la transcription asynchrone
async def transcribe_audio(file_path):
    try:
        # Chargement du modèle Whisper (peut être placé en dehors de la fonction si nécessaire)
        model = whisper.load_model('base')

        # Effectue la transcription
        result = await model.transcribe(file_path)

        # Stocke le résultat de la transcription
        transcription_result = result['text']
        transcription_id = str(uuid.uuid4())

        return transcription_result, transcription_id
    except Exception as e:
        raise e



@csrf_exempt
def generate_summary_view(request):
    if request.method == 'POST' and request.POST.get('transcription'):
        transcription = request.POST['transcription']
        # Here you would add logic to generate the summary
        summary = f"Summary of the transcription: {transcription[:200]}..."  # Mock summary
        return JsonResponse({'summary': summary})

    return JsonResponse({'error': 'POST method with transcription required'})


def download_transcription(request, transcription_id):
    # Here we would normally fetch the transcription from the database or cache
    # For simplicity, we are assuming the transcription is passed directly in the URL
    transcription = request.GET.get('transcription', 'No transcription found.')

    response = HttpResponse(transcription, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="transcription_{transcription_id}.txt"'
    return response


# views.py



def add_participant(request, session_id):
    session = get_object_or_404(Session, id=session_id)

    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            session.participants.add(participant)
            return redirect('session_detail', session_id=session.id)
    else:
        form = ParticipantForm()

    return render(request, 'add_participant.html', {'form': form, 'session': session})
