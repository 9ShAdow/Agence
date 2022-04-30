from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LieuForm(ModelForm):
    class Meta:
        model = models.Lieu
        fields = ('Pays', 'ville', 'visite_par_an', 'periode_plus_visite','periode_moins_visite','commentaires_faits')
        labels = {
            'pays': _('pays'),
            'ville' : _('ville'),
            'visite_par_an' : _('visite_par_an') ,
            'periode_plus_visite' : _('periode_plus_visite'),
            'periode_moins_visite' : _('periode_moins_visite'),
            'commentaires_faits' : _('commentaires_faits')
        }
        localized_fields = ('periode_plus_visite','periode_moins_visite',) #mettre en format une date français par defaut en format us
