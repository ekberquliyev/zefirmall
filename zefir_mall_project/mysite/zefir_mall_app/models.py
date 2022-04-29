from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class infocenter(models.Model):
    info_name = models.CharField(max_length=20,null=True,blank=True)
    info_subject = models.CharField(max_length=30,null=True,blank=True)
    info_text = models.CharField(max_length=60,null=True,blank=True)
    info_item = models.ImageField(upload_to = 'photo1',null=True,blank=True )
    info_link = models.URLField(null=True,blank=True)

class navbar(models.Model):
    name = models.CharField(max_length = 30, null = True, blank = True)
    link = models.CharField(max_length = 30, null=True, blank=True )
    def __str__(self):
        return f'{self.name}'

class about(models.Model):
    text = models.CharField(max_length=300, null=True, blank=True)

class rent(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(max_length=40, blank=True, null=True)
    pp = models.ImageField(upload_to = 'photo1', null = True, blank = True)
    number = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.name}'
class Footer(models.Model):
    logo_image = models.ImageField(upload_to = 'photo1', null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)

class foodcort(models.Model):
    foodname = models.CharField(max_length=40,null=True,blank=True)
    foodphoto = models.ImageField(upload_to = 'photo1', null=True, blank=True)
    foodlink = models.CharField(max_length=40,null=True,blank=True)

class company(models.Model):
    company_name  = models.CharField(max_length=200,null=True,blank=True)
    company_photo = models.ImageField(upload_to = 'photo1', null=True, blank=True)
    company_link = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        return f'{self.company_name}'