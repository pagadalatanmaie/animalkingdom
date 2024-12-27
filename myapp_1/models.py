from django.db import models

# Create your models here.
class cat(models.Model):
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    sound=models.CharField(max_length=20)
    
class bird(models.Model):
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    sound=models.CharField(max_length=20)
     
class snake(models.Model):
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    sound=models.CharField(max_length=20)

# ==========
class bear(models.Model):
    img_b1 = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    sound=models.CharField(max_length=20)
class chicken(models.Model):
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    sound=models.CharField(max_length=20)
class turtle(models.Model):
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    sound=models.CharField(max_length=20)
