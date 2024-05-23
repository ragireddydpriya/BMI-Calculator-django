from rest_framework import serializers

from .models import BMIModel

class BMISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BMIModel
        fields = ('name','gender', 'weight', 'height', 'BMI', 'BMI_category', 'BMI_HealthRisk')