from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from ckeditor.fields import RichTextField
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Author(models.Model):
    fish=models.CharField(max_length=200)
    def __str__(self):
        return self.fish
class Tarjimon(models.Model):
    fish=models.CharField(max_length=200)
    def __str__(self):
        return self.fish
class Sherlar(models.Model):
    nom=models.CharField(max_length=200)
    matn=RichTextField()
    autor=models.ForeignKey(Author, on_delete=models.CASCADE)
    vaqt=models.DateField()
    ctime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-vaqt']
    def __str__(self):
        return self.nom
class Hikoyalar(models.Model):
    nom=models.CharField(max_length=200)
    matn=RichTextField()
    autor=models.ForeignKey(Author, on_delete=models.CASCADE)
    vaqt=models.DateField()
    ctime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-vaqt']
    def __str__(self):
        return self.nom  
class Lavhalar(models.Model):
    nom=models.CharField(max_length=200)
    matn=RichTextField()
    autor=models.ForeignKey(Author, on_delete=models.CASCADE)
    vaqt=models.DateField()
    ctime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-vaqt']
    def __str__(self):
        return self.nom  
class Etyudlar(models.Model):
    nom=models.CharField(max_length=200)
    matn=RichTextField()
    autor=models.ForeignKey(Author, on_delete=models.CASCADE)
    vaqt=models.DateField()
    ctime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-vaqt']
    def __str__(self):
        return self.nom  
class Maqolalar(models.Model):
    nom=models.CharField(max_length=200)
    matn=RichTextField()
    autor=models.ForeignKey(Author, on_delete=models.CASCADE)
    vaqt=models.DateField()
    ctime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-vaqt']
    def __str__(self):
        return self.nom  
class EpikTarjima(models.Model):
    nom=models.CharField(max_length=200)
    matn=RichTextField()
    autor=models.ForeignKey(Author, on_delete=models.CASCADE)
    tarjimon=models.ForeignKey(Tarjimon, on_delete=models.CASCADE)
    vaqt=models.DateField()
    ctime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-vaqt']
    def __str__(self):
        return self.nom  
class LirikTarjima(models.Model):
    nom=models.CharField(max_length=200)
    matn=RichTextField()
    autor=models.ForeignKey(Author, on_delete=models.CASCADE)
    tarjimon=models.ForeignKey(Tarjimon, on_delete=models.CASCADE)
    vaqt=models.DateField()
    ctime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-vaqt']
    def __str__(self):
        return self.nom  
class DramatikTarjima(models.Model):
    nom=models.CharField(max_length=200)
    matn=RichTextField()
    autor=models.ForeignKey(Author, on_delete=models.CASCADE)
    tarjimon=models.ForeignKey(Tarjimon, on_delete=models.CASCADE)
    vaqt=models.DateField()
    ctime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-vaqt']
    def __str__(self):
        return self.nom  