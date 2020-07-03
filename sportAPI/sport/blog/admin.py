from django.contrib import admin
from.import models 
from django.utils.safestring import mark_safe

# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    actions = ('activate','desactivate')
    date_hierarchy = "date_add"
    list_per_page = 6 
    search_fields = ('nom',)
    def activate(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selection a été effectué avec succes')
    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self,request,queryset):  
        queryset.update(status=False)
        self.message_user(request,'la selection a été effectué avec succes')
    desactivate.short_description = "permet de desactiver le champs selectionner"

class CategorieAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info categorie",{"fields":["nom","description"]}),
                ("standard",{"fields":["status"]}) 
     ]


class TagAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info tag",{"fields":["nom","description"]}),
                ("standard",{"fields":["status"]}) 
     ]

class ArticleAdmin(CustomAdmin):
    list_display = ('nom','date','coach','date_add','date_update','image_view')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info article",{"fields":["nom","image","date","coach","tag"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class CommentaireAdmin(CustomAdmin):
    list_display = ('nom','article','date_add','date_update','image_view')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info carousol",{"fields":["nom","image","commentaire","article"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Categorie, CategorieAdmin)
_register(models.Tag,TagAdmin)
_register(models.Article,ArticleAdmin)
_register(models.Commentaire,CommentaireAdmin)
