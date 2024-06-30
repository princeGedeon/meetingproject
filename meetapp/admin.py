from django.contrib import admin
from .models import Office, SecretaireSeance, Session, Participant, Reunion, CompteRendu

# Office and SecretaireSeance Admins
@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'localisation')
    search_fields = ('nom', 'localisation')

@admin.register(SecretaireSeance)
class SecretaireSeanceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'role', 'office')
    search_fields = ('nom', 'prenom', 'email', 'role')
    list_filter = ('office',)

# Reunion and CompteRendu Admins
class ParticipantInline(admin.TabularInline):
    model = Reunion.participants.through
    extra = 1

@admin.register(Reunion)
class ReunionAdmin(admin.ModelAdmin):
    inlines = (ParticipantInline,)
    list_display = ('jour', 'heure_debut', 'heure_fin', 'session', 'secretaire')
    search_fields = ('jour', 'session__nom', 'secretaire__nom')
    list_filter = ('jour', 'session', 'secretaire')
    filter_horizontal = ('participants',)

@admin.register(CompteRendu)
class CompteRenduAdmin(admin.ModelAdmin):
    list_display = ('reunion', 'compte_rendu')
    search_fields = ('reunion__jour', 'compte_rendu')

# Session and Participant Admins
class ParticipantInline(admin.TabularInline):
    model = Session.participants.through
    extra = 1

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    inlines = (ParticipantInline,)
    list_display = ('nom', 'session_debut', 'session_fin')
    search_fields = ('nom',)

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    inlines = (ParticipantInline,)
    list_display = ('nom', 'prenom', 'email', 'role')
    search_fields = ('nom', 'prenom', 'email')
