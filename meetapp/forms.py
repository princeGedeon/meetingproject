from django import forms
from .models import Office, SecretaireSeance, Session, Participant, Reunion, CompteRendu

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = '__all__'

class SecretaireSeanceForm(forms.ModelForm):
    class Meta:
        model = SecretaireSeance
        fields = '__all__'

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

class ReunionForm(forms.ModelForm):
    class Meta:
        model = Reunion
        fields = '__all__'

class CompteRenduForm(forms.ModelForm):
    class Meta:
        model = CompteRendu
        fields = '__all__'
