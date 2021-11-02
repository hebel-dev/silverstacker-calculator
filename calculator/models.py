from django.core import validators
from django.db import models
from django.db.models.fields import CharField, DecimalField
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
from django.http import HttpResponse, request
import requests
import json




from datetime import datetime 

country_choice = (
    ('Poland', 'Polska'),
    ('USA', 'Stany Zjednoczone Ameryki'),
    ('France', 'Francja'),
    ('Russia', 'Rosja'),
)
category_choice = (
    ('circulation coin', 'moneta obiegowa'),
    ('commemorative coin','moneta okolicznościowa'),
    ('collector coin', 'moneta kolekcjonerska')

)

silver_purity_choice = (
    (Decimal("0.999"), '0.999'),
    (Decimal("0.925"), '0.925'),
    (Decimal("0.900"), '0.900'),
    (Decimal("0.835"), '0.835'),
    (Decimal("0.750"), '0.750'),
    (Decimal("0.680"), '0.680'),
    (Decimal("0.625"), '0.625') 
)

class Coin(models.Model):
    
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, choices=country_choice)
    category = models.CharField(max_length=50, choices= category_choice)
    year_first = models.IntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1865)])
    year_last = models.IntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1865)])
    silver_purity = models.DecimalField(max_digits=4, decimal_places=3, choices=silver_purity_choice)
    weight = models.DecimalField(max_digits=4, decimal_places=2, validators=[MaxValueValidator(1000), MinValueValidator(0)],)

    def __str__(self):
        return self.name
    
    @property
    def coin_weight_in_pure_Ag(self):
    
        v = self.silver_purity * self.weight
        return v
    
    

class SilverSpot(models.Model):
    spot = models.DecimalField(max_digits=17, decimal_places=15)
    price_data = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.spot)
        # return f'{self.spot}'
        # return '%s' % self.spot

   
  
    