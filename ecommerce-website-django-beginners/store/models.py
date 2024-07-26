from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null= True)
    email = models.CharField(max_length=50, null= True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, blank=False, null=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null = True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.order_items.all()
        total = sum([item.total_price for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.order_items.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
            

    
    @property
    def get_cart_items(self):
        orderitems = self.order_items.all()
        total = sum([item.quantity for item in orderitems])
        return total
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name='order_items')    
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def total_price(self):
        total = self.quantity * self.product.price
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100, null=True)    
    city = models.CharField(max_length=100, null=True)    
    state = models.CharField(max_length=100, null=True)    
    zipcode = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.address
    