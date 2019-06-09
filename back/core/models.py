from django.db import models

# Create your models here.

class UsdPrice(models.Model):
    
    clp_value = models.FloatField()
    date = models.DateField()

    def __str_(self):
        return "Valor del dolar el dia {}".format(self.date)
