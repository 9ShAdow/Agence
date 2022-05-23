from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from .models import Lieu
from django import forms

class LieuForm(ModelForm):
    class Meta:
        model = models.Lieu
        fields = ('pays', 'ville', 'visite_par_an', 'periode_plus_visite', 'periode_moins_visite', 'image_ville', 'commentaires_faits',)
        labels = {
            'pays': 'pays',
            'ville' : 'ville',
            'visite par an' : 'visite_par_an' ,
            'periode plus visite' : 'periode_plus_visite',
            'periode moins visite' : 'periode_moins_visite',
            'commentaires faits' : 'commentaires_faits',

            'image_ville': 'Image de la ville',
        }


class MonumentsForm(ModelForm):
    class Meta:
        model = models.Monuments
        fields = ('nom_monument', 'adresse_monument', 'date_construction', 'image_monument', 'lieu',)
        labels = {
            'nom monument': 'nom_monument',
            'adresse monument': 'adresse_monument',
            'date_construction': 'date de construction',
            'image_monument': 'Image du monument',
            'lieu': 'ville',
        }
        localized_fields = ('date_construction',)