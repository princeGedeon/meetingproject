# Importez les modules Django requis
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

# Importez les autres modules requis
import asyncio
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent

# Créez une vue Django pour gérer la transcription audio
@csrf_exempt  # Désactivez la vérification CSRF pour cette vue
@require_POST  # Cette vue accepte uniquement les requêtes POST
def transcribe_audio(request):
    # Définissez la région AWS
    region = "us-west-2"

    # Classe de gestion des événements de transcription
    class MyEventHandler(TranscriptResultStreamHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.transcription = ""

        async def handle_transcript_event(self, transcript_event: TranscriptEvent):
            results = transcript_event.transcript.results
            for result in results:
                for alt in result.alternatives:
                    self.transcription += alt.transcript + " "

    # Récupérez les échantillons audio envoyés depuis la requête POST en JSON
    data = json.loads(request.body)
    audio_samples = data['audio_samples']

    # Fonction principale pour transcrire l'audio
    async def transcribe(audio_samples):
        # Configuration du client avec la région AWS
        client = TranscribeStreamingClient(region=region)

        # Démarrez la transcription pour générer le flux asynchrone
        stream = await client.start_stream_transcription(
            language_code="en-US",
            media_sample_rate_hz=16000,
            media_encoding="pcm",
        )

        # Fonction pour écrire les chunks audio
        async def write_chunks(stream):
            for sample in audio_samples:
                chunk = bytes([sample])  # Convertir chaque échantillon en bytes
                await stream.input_stream.send_audio_event(audio_chunk=chunk)
            await stream.input_stream.end_stream()

        # Instanciez notre gestionnaire et commencez à traiter les événements
        handler = MyEventHandler(stream.output_stream)
        await asyncio.gather(write_chunks(stream), handler.handle_events())

        # Retourner la transcription obtenue
        return handler.transcription.strip()

    # Exécutez la fonction de transcription
    transcription = asyncio.run(transcribe(audio_samples))

    # Renvoyez la transcription dans la réponse JSON
    return JsonResponse({'transcription': transcription})
