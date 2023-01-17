from django.db import models
from datetime import timedelta, date
# Create your models here.

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=40)
    created_att = models.DateTimeField(auto_now_add=True)
    updated_att = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.catagory_name
    
class Suplier(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=150)
    address = models.CharField(max_length=560)
    product = models.CharField(max_length=160)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name



class Client(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=150)
    address = models.CharField(max_length=560)
    product = models.CharField(max_length=160)
    description = models.TextField()



    def __str__(self) -> str:
        return self.name


class Stock_Medisice(models.Model):
    medicine_name = models.CharField(max_length=160)
    Category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    Supplier = models.ForeignKey(Suplier, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quatity = models.IntegerField(default=0)
    exire_date = models.DateField()
    medicine_img = models.ImageField(upload_to='medicine_pic')

    def __str__(self) -> str:
        return self.medicine_name


class Medicine(models.Model):
    medicine = models.OneToOneField(Stock_Medisice, on_delete=models.CASCADE)
    selling_Price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    Description = models.TextField()


    def __str__(self) -> str:
        return str(self.medicine)


class Sale(models.Model):
    Product = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='sele_medicine')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quntity = models.IntegerField()
    sale_date = models.DateField(auto_now=True)
    

    
    def get_total_price(self):
        total = self.Product.selling_Price * self.quntity
        return total


