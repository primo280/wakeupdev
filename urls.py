from django.urls import path
from django.contrib.auth import views 
from . import views

urlpatterns = [
    path('', views.register, name='register'),
   path('login/', views.login_view, name='login'),
    path('payment/', views.payment, name="payment"),
     path('achat/<int:user_id>/', views.achat, name='achat'),
    path('panier/', views.panier, name='panier'),
    path('ajouter-au-panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('supprimer-du-panier/<int:item_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
]
