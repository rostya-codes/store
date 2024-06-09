from django.contrib import admin


from products.models import ProductCategory, Product

# Models registering
admin.site.register(Product)
admin.site.register(ProductCategory)
