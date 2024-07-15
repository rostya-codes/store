from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ ProductSerializers model """

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')  # or __all__
