from django.contrib import admin

from .models import Mensagem, Categoria, Tag

@admin.register(Categoria)                                      
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Tag)                                           
class TagAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria","criada_em")
    list_filter = ("categoria","tags")
    search_fields = ("titulo", "conteudo")
    autor = ("titulo", "autor")
    filter_horizontal = ("tags",)