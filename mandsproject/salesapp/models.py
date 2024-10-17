from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class saleArticles(models.Model):
    user = models.CharField()
    name = models.CharField()
    categorie = models.CharField()
    quantify = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ('saleArticle')
        verbose_name_plural = ('saleArticles')

    def __str__(self) -> str:
        return self.categorie
