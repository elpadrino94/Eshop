from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'catégorie'
        verbose_name_plural = 'catégories'

class Product(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField(max_length=155, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products')
    affliate_link = models.URLField("Lien affilié")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
