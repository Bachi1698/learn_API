from django.db import models

# Create your models here.
class Carousol(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/carousol')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta: 
        verbose_name = 'carousol'
        verbose_name_plural = 'carousols'

    def __str__(self):
        return self.titre

class SiteInfo(models.Model):
    slogan = models.CharField(max_length=255)
    carousol = models.ForeignKey(Carousol,on_delete=models.CASCADE,related_name='carousol_site')
    logo = models.ImageField(upload_to='logo/site')
    email = models.EmailField()
    tel = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'site info'
        verbose_name_plural = 'sites infos'

    def __str__(self):
        return self.slogan

class About(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="image/about")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'

    def __str__(self):
        return self.nom