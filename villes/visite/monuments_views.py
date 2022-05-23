from django.http import HttpResponseRedirect
from .forms import MonumentsForm
from django.shortcuts import render

from . import  models
# Cr eate your views here.
def ajoutmonuments(request):
    if request.method == "POST":
        form = MonumentsForm(request)
        if form.is_valid():
            monument = form.save()
            return HttpResponseRedirect("/visite/")
        else:
            return render(request,"monuments/ajout.html",{"form": form})
    else :
        form = MonumentsForm()
        return render(request,"monuments/ajout.html",{"form" : form})

def traitementmonuments(request):
    lform = MonumentsForm(request.POST)
    if lform.is_valid():
        monuments = lform.save()
        return HttpResponseRedirect("/visite/")
    else:
        return render(request,"monuments/ajout.html",{"form": lform})

def home(request):
    liste = list(models.Monuments.objects.all())
    return render(request, 'monuments/home.html', {'liste': liste})

def index(request):
    monuments = list(models.Monuments.objects.all())

    return render(request, 'monuments/index_monuments.html', {'monuments': monuments})

def affiche(request, id):
    monuments = models.Monuments.objects.get(pk=id)

    return render(request,"monuments/affiche.html",{"monuments": monuments})

def delete(request, id):
    monuments = models.Monuments.objects.get(pk=id)
    monuments.delete()
    return HttpResponseRedirect("/visite/affiche/" + str(monuments.lieu_id) + "/")

def update(request, id):
    monuments = models.Monuments.objects.get(pk=id)
    lform = MonumentsForm(monuments.dico())
    return render(request, "monuments/update.html", {"form": lform,"id":id})

def traitementupdate(request, id):
    lform = MonumentsForm(request.POST)
    if lform.is_valid():
        monuments = lform.save(commit=False)
        monuments.id = id;
        monuments.save()
        return HttpResponseRedirect("/visite/")
    else:
        return render(request, "monuments/update.html", {"form": lform, "id": id})