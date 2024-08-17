from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Panier, PanierProduit
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import CustomLoginForm

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            print(user) 
            if user is not None:
                login(request, user)
                return redirect('achat', user_id=user.id)
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = CustomLoginForm()
    return render(request, 'shop/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login') 
        else:
            print(form.errors)  # Ajoutez cette ligne pour imprimer les erreurs dans la console
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'shop/register.html', {'form': form})


def supprimer_du_panier(request, item_id):
    item = get_object_or_404(PanierProduit, id=item_id)
    item.delete()
    return redirect('panier')


def achat(request, user_id=None):
    if user_id is None:
        user_id = request.user.id  # Utilise l'ID de l'utilisateur connecté comme valeur par défaut
    produits = Produit.objects.all()
    context = {
        'user_id': user_id,
        'produits': produits
    }
    return render(request, 'shop/achat.html', context)


def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    panier, created = Panier.objects.get_or_create(utilisateur=request.user)
    panier_produit, created = PanierProduit.objects.get_or_create(panier=panier, produit=produit)
    panier_produit.quantite += 1  # Augmente la quantité du produit dans le panier
    panier_produit.save()
    return redirect('panier')  # Redirige vers la vue du panier

def panier(request):
    panier = get_object_or_404(Panier, utilisateur=request.user)
    panier_produits = PanierProduit.objects.filter(panier=panier)

    # Calcul du total
    total = sum(item.produit.prix * item.quantite for item in panier_produits)

    context = {
        'panier': panier,
        'panier_produits': panier_produits,
        'total': total
    }
    return render(request, 'shop/panier.html', context)
    

def payment (request):
    panier = get_object_or_404(Panier, utilisateur=request.user)
    panier_produits = PanierProduit.objects.filter(panier=panier)
    
    # Calcul du total
    total = sum(item.produit.prix * item.quantite for item in panier_produits)

    context = {
        'panier': panier,
        'panier_produits': panier_produits,
        'total': total
    }      
    total=='total'                                                            
    return render(request, 'shop/payment.html',  context)
def sucess (request):
    return render(request, 'shop/sucess.html')
