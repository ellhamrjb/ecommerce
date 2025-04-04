from django.db import models
import datetime

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    #correct the mistake of categories in admin page
    class Meta:
        verbose_name_plural='categories'


class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.EmailField(unique=True, null=True,blank=True)
    password=models.CharField(max_length=16)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0,decimal_places=2, max_digits=6)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=250,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/')
    #sale stuff
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name



class Order(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)
    address=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=15,default='')
    date=models.DateField(datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product

