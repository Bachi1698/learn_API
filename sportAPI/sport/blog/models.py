from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True) 

 
    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description =models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True) 

 
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom

class Article(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/article')
    date = models.DateField()
    coach = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag,related_name='tag_article')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True) 

 
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article_commentaire')
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='commentaire/image')
    commentaire = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True) 

 
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.nom

