from django.db import models

# Create your models here.
class Video(models.Model):
    last_video = models.URLField(null=True)
    titre = models.CharField(max_length=255)
    date = models.DateField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.titre

class Match(models.Model):
    titre = models.CharField(max_length=255)
    date = models.DateField()
    heure = models.TimeField()
    equipeA = models.CharField(max_length=255)
    equipeB = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta:
        verbose_name = 'match'
        verbose_name_plural = 'matchs'

    def __str__(self):
        return self.titre

class Joueur(models.Model):
    image = models.ImageField(upload_to='image/joueur')
    poste = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta:
        verbose_name = 'joueur'
        verbose_name_plural = 'joueurs'

    def __str__(self):
        return self.poste

class Sponsor(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/sponsor')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta:
        verbose_name = 'sponsor'
        verbose_name_plural = 'sponsors'

    def __str__(self):
        return self.nom

class Entrainement(models.Model):
    nom = models.CharField(max_length=255)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta:
        verbose_name = 'Entrainement'
        verbose_name_plural = 'Entrainements'

    def __str__(self):
        return self.nom

class Classement(models.Model):
    rang = models.IntegerField()
    match_null = models.IntegerField()
    match_gagner = models.IntegerField()
    match_defaite = models.IntegerField()
    equipe = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta:
        verbose_name = 'Classement'
        verbose_name_plural = 'Classements'

    def __str__(self):
        return self.equipe