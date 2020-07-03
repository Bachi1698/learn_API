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

class SiteInfoAdmin(CustomAdmin): 
    list_display = ('slogan','email','tel','date_add','date_update','logo_view')
    search_fields = ('slogan',)
    list_display_links = ['slogan']
    ordering = ['slogan']
    fieldsets = [
                ("info commentaire",{"fields":["slogan","email","tel","carousol","logo"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))

def _register(model,admin_class):
    admin.site.register(model,admin_class)

class ReseauAdmin(CustomAdmin):
    list_display = ('nom','lien','date_add','date_update')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info commentaire",{"fields":["nom","lien","icone"]}),
                ("standard",{"fields":["status"]}) 
     ]


class AboutAdmin(CustomAdmin):
    list_display = ('titre','date_add','date_update','image_view')
    search_fields = ('titre',)
    list_display_links = ['titre']
    ordering = ['titre']
    fieldsets = [
                ("info commentaire",{"fields":["staff","titre","description","image"]}),
                ("standard",{"fields":["status"]}) 
     ]


    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class ContactAdmin(CustomAdmin):
    list_display = ('nom','email','tel','date_add','date_update')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info commentaire",{"fields":["nom","sujet","tel","email","message"]}),
                ("standard",{"fields":["status"]}) 
     ]

def _register(model,admin_class):
    admin.site.register(model,admin_class)

class StaffAdmin(CustomAdmin):
    list_display = ('role','contact','date_add','date_update','image_view')
    search_fields = ('role',)
    list_display_links = ['role']
    ordering = ['role']
    fieldsets = [
                ("info commentaire",{"fields":["role","contact","image"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model,admin_class)

class CarousolAdmin(CustomAdmin):
    list_display = ('titre','date_add','date_update','image_view')
    search_fields = ('titre',)
    list_display_links = ['titre']
    ordering = ['titre']
    fieldsets = [
                ("info commentaire",{"fields":["titre","image"]}),
                ("standard",{"fields":["status"]}) 
     ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))

class NewsletterAdmin(CustomAdmin):
    list_display = ('nom','email','date_add','date_update')
    search_fields = ('nom',)
    list_display_links = ['nom']
    ordering = ['nom']
    fieldsets = [
                ("info newsletter",{"fields":["nom","email"]}),
                ("standard",{"fields":["status"]}) 
     ]
def _register(model,admin_class):
    admin.site.register(model,admin_class)

_register(models.SiteInfo, SiteInfoAdmin)
_register(models.About,AboutAdmin)
_register(models.Carousol,CarousolAdmin)
_register(models.Staff,StaffAdmin)
_register(models.Reseau,ReseauAdmin)
_register(models.Contact,ContactAdmin)
_register(models.Newsletter,NewsletterAdmin)