from django.contrib import admin
from .models import CustomUser, UserProfile, Produit, Panier, PanierProduit
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name','username', 'last_name','is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)

# Ensure this block is only present once in your codebase
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(UserProfile, UserProfileAdmin)

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    search_fields = ('nom',)
    list_filter = ('prix',)
    
admin.site.register(Produit, ProduitAdmin)

class PanierProduitInline(admin.TabularInline):
    model = PanierProduit
    extra = 1

class PanierAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'total')
    inlines = [PanierProduitInline]

admin.site.register(Panier, PanierAdmin)
