from rest_framework import viewsets

from .serializers import BMISerializer
from .models import BMIModel


class BMIViewSet(viewsets.ModelViewSet):
    queryset = BMIModel.objects.all().order_by('name')
    serializer_class = BMISerializer