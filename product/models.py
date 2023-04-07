from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class Review(models.Model):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
