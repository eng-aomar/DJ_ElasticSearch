from django.db import models

# Create your models here.
class Product(models.Model):
    id =models.CharField(max_length=200, primary_key=True)
    type =models.TextField( null=True, blank=True)
    arlabel =models.TextField( null=True, blank=True)
    enlabel =models.TextField( null=True, blank=True)
    araliases =models.TextField( null=True, blank=True)
    enaliases =models.TextField( null=True, blank=True)
    ardescription =models.TextField( null=True, blank=True)
    endescription =models.TextField( null=True, blank=True)
    maincategory =models.TextField( null=True, blank=True)
    arwiki =models.TextField( null=True, blank=True)
    enwiki =models.TextField( null=True, blank=True)   
    arwikiquote = models.TextField( null=True, blank=True) 
    enwikiquote = models.TextField( null=True, blank=True)

    def get_absolute_url(self):
        return f"products/{self.id}"