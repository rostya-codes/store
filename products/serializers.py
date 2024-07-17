from rest_framework import fields, serializers

from products.models import Basket, Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    """ ProductSerializers model """

    # Для отображения названия одежды
    category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())

    class Meta:
        model = Product

        # or    fields = __all__(but not recommendated)
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')


class BasketSerializer(serializers.ModelSerializer):

    product = ProductSerializer()  # Передается полная информация про продукт, а не только id
    sum = fields.FloatField(required=False)
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'sum', 'total_sum', 'total_quantity', 'created_timestamp')
        read_only_fields = ('created_timestamp',)

    def get_total_sum(self, obj):
        """`get` at the beginning of name is necessarily"""
        return Basket.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_quantity()
