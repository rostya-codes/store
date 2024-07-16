from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ ProductSerializers model """

    category = serializers.SlugRelatedField(slug_field='name', read_only=True)  # Для отображения названия одежды

    class Meta:
        model = Product

        # or    fields = __all__(but not recommendated)
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')
