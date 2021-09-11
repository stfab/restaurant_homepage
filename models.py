from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 2000)
    image = models.ImageField()
    index = models.BooleanField(default=False)   
    
    def __str__(self):
        return "%s, Index: %s" % (self.title,self.index)
    
class Menu(models.Model):    
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    
class Dish(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)  
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    description = models.CharField(max_length = 2000)  
    
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField()    
    position = models.CharField(max_length = 200)
    info = models.CharField(max_length = 200)
        
    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    name = models.CharField(max_length = 200)
    groupsize = models.IntegerField(validators=[MinValueValidator(0)])
    email = models.EmailField()
    appointment = models.DateTimeField()
    miscellaneous = models.TextField(blank=True)
        
    def __str__(self):
        return str(self.name)+", "+str(self.appointment)
