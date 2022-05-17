from django.db import models


# Create your models here.

class Lieu(models.Model):  # déclare la classe Lieu héritant de la classe Model, classe de base des modèles
    pays = models.CharField(max_length=100)  # défini un champs de type texte de 100 caractères maximum
    ville = models.CharField(max_length=100)
    periode_plus_visite = models.DateField(blank=True, null=True)
    periode_moins_visite = models.DateField(blank=True, null=True)   # champs de type date, pouvant être null ou ne pas être rempli
    visite_par_an = models.CharField(max_length=100)  # champs de type entier devant être obligatoirement rempli
    commentaires_faits = models.TextField(null=True, blank=True)  # champs de type text long

    def __str__(self):
        chaine = f"La ville de  {self.ville} se trouve en {self.pays} elle a  {self.visite_par_an} visite par an "
        return chaine

    def dico(self):
        return {"pays": self.pays, "ville": self.ville, "periode_plus_visite": self.periode_plus_visite, "periode_moins_visite": self.periode_moins_visite,
                "visite_par_an": self.visite_par_an, "commentaires_faits": self.commentaires_faits}

class Monuments(models.Model):
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, null ="true")
    nom_monument = models.CharField(max_length=100)
    adresse_monument = models.CharField(max_length=100)
    date_construction = models.DateField(blank=True, null=True)

    def __str__(self):
        chaine = f"Le monument  {self.nom_monument} se trouve a {self.lieu_ville} son adresse est {self.adresse_monument} et il a été construit en {self.date_construction}"
        return chaine
    def dico(self):
        return {"lieu": self.lieu, "nom_monument": self.nom_monument, "adresse_monument ": self.adresse_monument, "date_construction": self.date_construction}



