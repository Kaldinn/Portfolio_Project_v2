from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    
class Budget(models.Model):
    TYPE_CHOICES = [
        ('usluga', 'Usługa'),
        ('material', 'Materiał'),
    ]
    TAX_CHOICES = [
        (8, '8%'),
        (23, '23%'),
    ]
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    tax = models.IntegerField(choices=TAX_CHOICES)
    price = models.IntegerField(default=0)
