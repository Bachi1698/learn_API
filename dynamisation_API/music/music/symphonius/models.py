from django.db import models

# Create your models here.
class Tour(models.Model):
    artiste = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    date = models.DateField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'tour'
        verbose_name_plural = 'tours'

    def __str__(self):
        return self.titre
    
class Video(models.Model):
    video = models.FileField(upload_to='video/video')
    titre = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.titre

class Album(models.Model):
    image = models.ImageField(upload_to="album/image")
    titre = models.CharField(max_length=255)
    annee = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'album'
        verbose_name_plural = 'albums'

    def __str__(self):
        return self.titre

class Musique(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE,related_name="album_musque")
    musique = models.FileField(upload_to="musique/musique")
    titre = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'musique'
        verbose_name_plural = 'musiques'

    def __str__(self):
        return self.titre

class Equipe(models.Model):
    titre = models.CharField(max_length=255)
    competence = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="image/equipe")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta: 
        verbose_name = 'equipe'
        verbose_name_plural = 'equipes'

    def __str__(self):
        return self.titre

class Gallerie(models.Model):
    image = models.ImageField(upload_to="image/gallerie")
    lien = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'gallerie'
        verbose_name_plural = 'galleries'

    def __str__(self):
        return self.lien