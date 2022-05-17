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

]