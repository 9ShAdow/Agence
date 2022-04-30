from django.db import models


# Create your models here.

class Lieu(models.Model):  # déclare la classe Lieu héritant de la classe Model, classe de base des modèles
    Pays = models.CharField(max_length=100)  # défini un champs de type texte de 100 caractères maximum
    ville = models.CharField(max_length=100)
    periode_plus_visite = models.DateField(blank=True, null=True)
    periode_moins_visite = models.DateField(blank=True, null=True)   # champs de type date, pouvant être null ou ne pas être rempli
    visite_par_an = models.IntegerField(blank=False)  # champs de type entier devant être obligatoirement rempli
    commentaires_faits = models.TextField(null=True, blank=True)  # champs de type text long

    def __str__(self):
        chaine = f"La ville de  {self.ville} se trouve en {self.Pays} elle as  {self.visite_par_an} visite par an "
        return chaine

    def dico(self):
        return {"Pays": self.pays, "Ville": self.ville, "periode_plus_visite": self.periode_plus_visite, "periode_moins_visite": self.periode_moins_visite,
                "visite_par_an": self.visite_par_an, "commentaires_faits": self.commentaires_faits}




