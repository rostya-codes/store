from django.db import models

from products.models import Basket
from users.models import User


class Order(models.Model):
    """ Order Django ORM model """

    # Statuses
    CREATED = 0  # Заказ создан
    PAID = 1  # Заказ оплачен
    ON_WAY = 2  # Заказ в пути
    DELIVERED = 3  # Заказ доставлен
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)  # Адрес доставки
    basket_history = models.JSONField(default=dict)  # Словарь в котором хранится информация о продукте
    created = models.DateTimeField(auto_now_add=True)  # Created time
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)  # С какого аккаунта был создан заказ

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = self.PAID
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum()),
        }
        baskets.delete()
        self.save()
