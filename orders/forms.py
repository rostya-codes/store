from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    """ OrderForm Django model """

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')
