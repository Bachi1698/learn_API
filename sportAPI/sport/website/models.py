from django.db import models

# Create your models here. 
class Staff(models.Model):
    image = models.ImageField(upload_to='image/staff')
    contact = models.IntegerField()
    role = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True) 

 
    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staffs'

    def __str__(self):
        return self.role

class Reseau(models.Model):
    ICONE = [
        ('facebook','fa fa-facebook'),
        ('twitter','fa fa-twitter'),
        ('instagram','fa fa-instagram'),
    ]
    lien = models.URLField()
    nom = models.CharField(max_length=255)
    icone = models.CharField(max_length=255,choices=ICONE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta:
        verbose_name = 'reseau'
        verbose_name_plural = 'reseau'

    def __str__(self):
        return self.nom

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

class Newsletter(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

 
    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'

    def __str__(self):
        return self.nom

class SiteInfo(models.Model):
    carousol = models.ForeignKey(Carousol,on_delete=models.CASCADE,related_name='carousol_site')
    logo = models.ImageField(upload_to='logo/site')
    email = models.EmailField()
    mapping = models.TextField()
    slogan = models.CharField(max_length=255)
    tel = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'site info'
        verbose_name_plural = 'sites infos'

    def __str__(self):
        return self.slogan

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    sujet = models.CharField(max_length=255)
    email = models.EmailField()
    tel =models.IntegerField()
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.nom

class About(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="staff_about")
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="iamge/about")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'

    def __str__(self):
        return self.titre
