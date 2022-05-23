from django.db import models
from django import forms


# Create your models here.

class Lieu(models.Model):  # déclare la classe Lieu héritant de la classe Model, classe de base des modèles
    pays = models.CharField(max_length=100)  # défini un champs de type texte de 100 caractères maximum
    ville = models.CharField(max_length=100)
    periode_plus_visite = models.CharField(max_length=100 ,default = None)
    periode_moins_visite = models.CharField(max_length=100 ,default = None)   # champs de type date, pouvant être null ou ne pas être rempli
    visite_par_an = models.CharField(max_length=100)  # champs de type entier devant être obligatoirement rempli
    commentaires_faits = models.TextField(null=True, blank=True)  # champs de type text long
    image_ville = models.ImageField(null=True, blank=True, upload_to="images/")


    def __str__(self):
        chaine = str(f"La ville de  {self.ville} se trouve en {self.pays} elle a  {self.visite_par_an} visite par an ")
        return chaine

    def dico(self):
        return {"pays": self.pays, "ville": self.ville, "periode_plus_visite": self.periode_plus_visite, "periode_moins_visite": self.periode_moins_visite,
                "visite_par_an": self.visite_par_an, "commentaires_faits": self.commentaires_faits, "image_ville": self.image_ville}

class Monuments(models.Model):

    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, default=None)
    nom_monument = models.CharField(max_length=100)
    adresse_monument = models.CharField(max_length=100)
    date_construction = models.DateField(blank=True, null=True)
    image_monument = models.ImageField(null=True, blank=True, upload_to="media/images")

    def __str__(self):
         return self.nom_monument

    def dico(self):
        return {"nom_monument": self.nom_monument, "adresse_monument": self.adresse_monument, "date_construction": self.date_construction, "image_monument": self.image_monument, "lieu": self.lieu}



