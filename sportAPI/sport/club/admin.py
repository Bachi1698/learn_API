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

class VideoAdmin(CustomAdmin):
    list_display = ('titre','last_video','date_add','date_update')
    search_fields = ('titre',)
    list_display_links = ['titre']
    ordering = ['titre']
    fieldsets = [
                ("info commentaire",{"fields":["titre","last_video"]}),
                ("standard",{"fields":["status"]}) 
     ]


class MatchAdmin(CustomAdmin):
    list_display = ('titre','date','heure','equipeA','equipeB','date_add','date_update')
    search_fields = ('titre',)
    list_display_links = ['titre']
    ordering = ['titre']
    fieldsets = [
                ("info commentaire",{"fields":["date","titre","heure","equipeA","equipeB"]}),
                ("standard",{"fields":["status"]}) 
     ]


class JoueurAdmin(CustomAdmin):
    list_display = ('poste','date_add','date_update','image_view')
    search_fields = ('poste',)
    list_display_links = ['poste']
    ordering = ['poste']
    fieldsets = [
                ("info commentaire",{"fields":["poste","image"]}),
                ("standard",{"fields":["status"]}) 
     ]


    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class SponsorAdmin(CustomAdmin):
    list_display = ('nom','date_add','date_update','image_view')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info commentaire",{"fields":["nom","image"]}),
                ("standard",{"fields":["status"]}) 
     ]


    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class EntrainementAdmin(CustomAdmin):
    list_display = ('nom','date','heure_debut','heure_fin','date_add','date_update')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info commentaire",{"fields":["nom","date","heure_debut","heure_fin"]}),
                ("standard",{"fields":["status"]}) 
     ]


class ClassementAdmin(CustomAdmin):
    list_display = ('rang','match_null','match_gagner','equipe','match_defaite','date_add','date_update')
    search_fields = ('equipe',)
    list_display_links = ['equipe']
    ordering = ['equipe']
    fieldsets = [
                ("info commentaire",{"fields":["rang","equipe","match_null","match_gagner","match_defaite"]}),
                ("standard",{"fields":["status"]}) 
     ]



def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.Video, VideoAdmin)
_register(models.Match,MatchAdmin)
_register(models.Joueur,JoueurAdmin)
_register(models.Sponsor,SponsorAdmin)
_register(models.Entrainement,EntrainementAdmin)
_register(models.Classement,ClassementAdmin)