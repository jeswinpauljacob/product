


from django.db import models
from django.urls import reverse

class product(models.Model):
    Productname = models.CharField(max_length=200)
    Price = models.IntegerField()

    def __str__(self):
        return self.Productname

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})