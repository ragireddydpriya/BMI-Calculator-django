from decimal import Decimal
from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ("1", "Female"),
    ("2", "Male"),
)

category_Healthrisk_dict = {
    "under weight" : "Malnutrition risk",
    "Normal weight" : "Low risk",
    "over weight" : "Enhanced risk",
    "Moderately obese" : "Medium risk",
    "Severly obese" : "High risk",
    "Very severly obese" : "Very high risk"
}

class BMIModel(models.Model):
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = '1')
    weight = models.DecimalField(max_digits=6,decimal_places=3)
    height = models.DecimalField(max_digits=6,decimal_places=3)

    def calculator(self,weight,height):
        return Decimal(weight/(height/100)**2)

    @property
    def BMI(self):
        return self.calculator(self.weight, self.height)

    def category_Select(self,BMI):
        if BMI <= 18.4:
            category = "under weight"
        elif BMI >= 18.5 and BMI <= 24.9:
            category = "Normal weight"
        elif BMI >= 25 and BMI <= 29.9:
            category = "over weight"
        elif BMI >= 30 and BMI <= 34.9:
            category = "Moderately obese"
        elif BMI >= 35 and BMI <= 39.9:
            category = "Severly obese"
        elif BMI >= 40:
            category = "Very severly obese"
        return category

    @property
    def BMI_category(self):
        return self.category_Select(self.BMI)

    def mapping(self,category):
        if category in category_Healthrisk_dict.keys():
            return category_Healthrisk_dict[category]

    @property
    def BMI_HealthRisk(self):
        return self.mapping(self.BMI_category)


    def __str__(self):
        return str(self.name)