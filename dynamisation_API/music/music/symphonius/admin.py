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

class TourAdmin(CustomAdmin):
    list_display = ('artiste','titre','date','date_add','date_update')
    search_fields = ('artiste',)
    list_display_links = ['artiste']
    ordering = ['artiste']
    fieldsets = [
                ("info commentaire",{"fields":["artiste","titre","date"]}),
                ("standard",{"fields":["status"]}) 
     ]


class VideoAdmin(CustomAdmin):
    list_display = ('titre','date_add','date_update','status')
    search_fields = ('titre',)
    list_display_links = ['titre']
    ordering = ['titre']
    fieldsets = [
                ("info commentaire",{"fields":["titre","video"]}),
                ("standard",{"fields":["status"]}) 
     ]

class MusiqueAdmin(CustomAdmin):
    list_display = ('titre','date_add','date_update','musique')
    search_fields = ('titre',)
    list_display_links = ['titre']
    ordering = ['titre']
    fieldsets = [
                ("info commentaire",{"fields":["titre","musique","album"]}),
                ("standard",{"fields":["status"]}) 
     ]

class EquipeAdmin(CustomAdmin):
    list_display = ('titre','competence','date_add','date_update','image_view')
    search_fields = ('titre',)
    list_display_links = ['titre']
    ordering = ['titre']
    fieldsets = [
                ("info commentaire",{"fields":["titre","competence","description","image"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class AlbumAdmin(CustomAdmin):
    list_display = ('titre','annee','date_add','date_update','image_view')
    search_fields = ('titre',)
    list_display_links = ['titre']
    ordering = ['titre']
    fieldsets = [
                ("info commentaire",{"fields":["titre","annee","image"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class GallerieAdmin(CustomAdmin):
    list_display = ('lien','date_add','date_update','image_view')
    search_fields = ('lien',)
    list_display_links = ['lien']
    ordering = ['lien']
    fieldsets = [
                ("info commentaire",{"fields":["lien","image"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


def _register(model,admin_class):
    admin.site.register(model,admin_class)


_register(models.Tour, TourAdmin)
_register(models.Video,VideoAdmin)
_register(models.Musique,MusiqueAdmin)
_register(models.Album,AlbumAdmin)
_register(models.Equipe,EquipeAdmin)
_register(models.Gallerie,GallerieAdmin)