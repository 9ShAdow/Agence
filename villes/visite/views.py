from django.http import HttpResponseRedirect
from .forms import LieuForm
from django.shortcuts import render

from . import  models
# Cr eate your views here.
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
    lform = LieuForm(request.POST, request.FILES)
    if lform.is_valid():
        lieu = lform.save()
        return HttpResponseRedirect("/visite/"  )
    else:
        return render(request,"visite/ajout.html",{"form": lform})

def home(request):
    liste = list(models.Lieu.objects.all())
    return render(request, 'visite/home.html', {'liste': liste})

def index(request):
    liste = list(models.Lieu.objects.all())
    return render(request, 'visite/index.html', {'liste': liste})

def affiche(request, id):
    lieu = models.Lieu.objects.get(pk=id)
    monuments = models.Monuments.objects.filter(lieu= lieu.id)
    return render(request,"visite/affiche.html",{"lieu" : lieu, "monuments": monuments})


def delete(request, id):
    lieu = models.Lieu.objects.get(pk=id)
    lieu.delete()
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










