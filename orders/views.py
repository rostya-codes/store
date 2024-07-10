from django.views.generic.edit import CreateView


class OrderCreateView(CreateView):
    template_name = 'orders/order_create.html'
