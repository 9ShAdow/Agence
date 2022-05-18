from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LieuForm(ModelForm):
    class Meta:
        model = models.Lieu
        fields = ('pays', 'ville', 'visite_par_an', 'periode_plus_visite','periode_moins_visite','commentaires_faits', 'monuments')
        labels = {
            'pays': _('pays'),
            'ville' : _('ville'),
            'visite par an' : _('visite_par_an') ,
            'periode plus visite' : _('periode_plus_visite'),
            'periode moins visite' : _('periode_moins_visite'),
            'commentaires faits' : _('commentaires_faits'),
            'monuments' : _('monuments')
        }
        localized_fields = ('periode_plus_visite','periode_moins_visite',) #mettre en format une date français par defaut en format us

class MonumentsForms(ModelForm):
    class Meta:
        model = models.Monuments
        fields = ('nom_monument', 'adresse_monument', 'date_construction',)
        labels = {
            'nom monument': _('nom_monument'),
            'adresse monument': _('adresse_monument'),
            'date_construction': _('date_construction'),

        }
        localized_fields = ('date_construction',)