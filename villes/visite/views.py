from django.http import HttpResponseRedirect
from .forms import LieuForm
from django.shortcuts import render

from . import  models
# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = LieuForm(request)
        if form.is_valid():
            lieu = form.save()
            return HttpResponseRedirect("/visite/")
        else:
            return render(request,"visite/ajout.html",{"form": form})
    else :
        form = LieuForm()
        return render(request,"visite/ajout.html",{"form" : form})

def traitement(request):
    lform = LieuForm(request.POST)
    if lform.is_valid():
        lieu = lform.save()
        return HttpResponseRedirect("/visite/")
    else:
        return render(request,"visite/ajout.html",{"form": lform})


def index(request):
    liste = list(models.Lieu.objects.all())
    return render(request, 'visite/index.html', {'liste': liste})

def affiche(request, id):
    lieu = models.Lieu.objects.get(pk=id)
    return render(request,"visite/affiche.html",{"lieu" : lieu})

def effacer(request, id):
    lieu = models.Lieu.objects.get(pk=id)
    lieu.effacer()
    return HttpResponseRedirect("/visite/")

def update(request, id):
    lieu = models.Lieu.objects.get(pk=id)
    lform = LieuForm(lieu.dico())
    return render(request, "visite/update.html", {"form": lform,"id":id})

def traitementupdate(request, id):
    lform = LieuForm(request.POST)
    if lform.is_valid():
        lieu = lform.save(commit=False)
        lieu.id = id;
        lieu.save()
        return HttpResponseRedirect("/visite/")
    else:
        return render(request, "visite/update.html", {"form": lform, "id": id})



