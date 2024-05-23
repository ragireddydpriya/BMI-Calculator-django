from django.test import TestCase
from api.models import BMIModel
from decimal import Decimal
# Create your tests here.

class BMIModelTestCase(TestCase):
    def setUp(self):
        BMIModel.objects.create(name="kushi",gender="2",weight=	"15.000",height="65.000")


    def test_animals_can_speak(self):
        Kushi = BMIModel.objects.get(name="kushi")
        self.assertEqual(Kushi.BMI, Decimal("35.50295857988165680473372781"))
        self.assertEqual(Kushi.BMI_category, "Severly obese")
        self.assertEqual(Kushi.BMI_HealthRisk, "High risk")


