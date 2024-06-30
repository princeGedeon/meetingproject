from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Office(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    localisation = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class SecretaireSeance(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

    def faire_transcription(self):
        # Define the logic here
        pass

    def generer_compte_rendu(self):
        # Define the logic here
        pass

    def ajouter_participant(self, participant):
        # Define the logic here
        pass

    def creer_reunion(self, reunion):
        # Define the logic here
        pass

class Session(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    session_debut = models.DateTimeField()
    session_fin = models.DateTimeField()
    image = models.ImageField(upload_to='session_images/', blank=True, null=True, default='telechargement.png')
    participants = models.ManyToManyField('Participant', related_name='sessions', blank=True)

    def __str__(self):
        return self.nom


class Participant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Reunion(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, related_name='reunions')
    jour = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    secretaire = models.ForeignKey(SecretaireSeance, on_delete=models.CASCADE)

    def __str__(self):
        return f'Reunion on {self.jour}'

class CompteRendu(models.Model):
    reunion = models.OneToOneField(Reunion, on_delete=models.CASCADE)
    compte_rendu = models.TextField()

    def __str__(self):
        return f'CompteRendu for {self.reunion}'
