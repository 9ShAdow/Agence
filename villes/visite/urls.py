from django.urls import path
from . import views, monuments_views

urlpatterns = [
    path('',views.home),
    path('index/',views.index),
    path('ajout/',views.ajout),
    path("traitement/",views.traitement),
    path("affiche/<int:id>/",views.affiche),
    path("delete/<int:id>",views.delete),
    path("update/<int:id>",views.update),
    path("traitementupdate/<int:id>",views.traitementupdate),
    # views monuments
    path('',monuments_views.home),
    path('indexmonuments/',monuments_views.index),
    path('ajoutmonuments/',monuments_views.ajoutmonuments),
    path("traitementmonuments/",monuments_views.traitement),
    path("affichemonuments/<int:id>/",monuments_views.affiche),
    path("deletemonuments/<int:id>",monuments_views.delete),
    path("updatemonuments/<int:id>",monuments_views.update),
    path("traitementupdatemonuments/<int:id>",monuments_views.traitementupdate),

]