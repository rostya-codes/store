from django.db import models

from users.models import User


class ProductCategory(models.Model):
    """ ProductCategory model """

    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)  # Может быть пустым

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Product model """

    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'


class BasketQuerySet(models.QuerySet):
    """ BasketQuerySet """

    def total_sum(self):
        """Returns total sum of all baskets(products)"""
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        """Returns total quantity of all baskets(products)"""
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    """ Basket model """

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        """Returns sum of baskets(products in a basket)"""
        return self.product.price * self.quantity
