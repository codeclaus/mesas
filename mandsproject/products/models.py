from django.db import models


# Create your models here.


class categories(models.Model):
    name = models.CharField()

    class Meta:
        verbose_name = ('categorie')
        verbose_name_plural = ('categories')

    def __str__(self) -> str:
        return self.name


class productsP(models.Model):
    name = models.CharField()
    description = models.TextField()
    price = models.FloatField()
    available = models.BooleanField(default=False)
    categorie = models.ForeignKey(categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self) -> str:
        return self.name
