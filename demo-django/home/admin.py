from django.contrib import admin

from .models import Mensagem, Categoria

@admin.register(Categoria)                                       # ← novo
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria","criada_em")
    list_filter = ("categoria",)
    search_fields = ("titulo", "conteudo")
    autor = ("titulo", "autor")