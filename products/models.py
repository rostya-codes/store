from django.db import models


class ProductCategory(models.Model):
    """ ProductCategory model """

    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)  # Может быть пустым

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Product model """

    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
