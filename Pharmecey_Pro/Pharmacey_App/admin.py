from django.contrib import admin
from .models import Catagory, Suplier, Stock_Medisice, Medicine, Sale, Client
# Register your models here.

admin.site.register(Catagory)
admin.site.register(Suplier)
admin.site.register(Stock_Medisice)
admin.site.register(Medicine)
admin.site.register(Sale)
admin.site.register(Client)