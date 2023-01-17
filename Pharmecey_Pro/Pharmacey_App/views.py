from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Catagory, Stock_Medisice, Suplier, Medicine, Sale, Client
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from django.contrib.auth.models import User
# Create your views here.



@login_required()
def Deshbord(request):
    # get tomorrow or last 7 days date
    tomorrow = timedelta(days=-1)
    last7_days = timedelta(days=-7)
    
    
    Date = date.today()
    yesterday_date = Date + tomorrow
    last_7days_date = Date + last7_days
    
    
    # get data by filtering sale date
    
    today_sale = Sale.objects.filter(sale_date=Date)
    yesterday_sale = Sale.objects.filter(sale_date=yesterday_date)
    last7dyas_sale = Sale.objects.filter(sale_date=last_7days_date)
    
    # store totall sale from for loop
    today_total_sale = 0
    yesterday_total_sale = 0
    befor7_days_total = 0
    
    for i in today_sale:
        today_total_sale += i.Product.selling_Price
    
    for i in yesterday_sale:
        yesterday_total_sale += i.Product.selling_Price
    
    for i in last7dyas_sale:
        yesterday_total_sale += i.Product.selling_Price
    
    
    # get supplier
    suplier = Suplier.objects.all()
    # get all user
    user = User.objects.all().count()
    
    # get all date expeired medicine
    
    medicine = Medicine.objects.all()
    list = []
    for i in medicine:
        
        if (i.medicine.exire_date) <= Date:
            list.append(i)
        
        

            
        
    # Get all catagory here
    catagory = Catagory.objects.all().count()
    
    # Get all medicine here
    medicine = Medicine.objects.all().count()

    

    Total = Sale.objects.all()
    total_sale = 0
    for i in Total:
        total_sale += i.Product.selling_Price
    

    Stock_out = Stock_Medisice.objects.filter(quatity=0).count()
    Stock_out = Stock_Medisice.objects.filter(quatity=0).count()

    context = {
        'today_total_sale':today_total_sale,
        'yesterday_total_sale':yesterday_total_sale,
        'suplier':suplier,
        'user':user,
        'catagory':catagory,
        'medicine':medicine,
        'today_sale':today_sale,
        'total_sale':total_sale,
        'Stock_out':Stock_out,
    }
        
    return render(request, 'HOD/Deshbord.html', context)


@login_required()
def Add_Category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        print(category)
        category = Catagory(catagory_name=category)
        category.save()
        messages.success(request, 'Category Added Successfully!')
        return redirect('Pharmacey_App:Add_Category')
    
    return render(request, 'HOD/add_cat.html')
@login_required()
def View_Category(request):
    categorys = Catagory.objects.all()
    categorys2 = Catagory.objects.all()
    context = {
        'categorys':categorys,
    }
    
    return render(request, 'HOD/view_category.html', context)


@login_required()    
def Edit_Cat(request, id):
    category = Catagory.objects.get(id=id)
    
    context = {
        'category':category
    }
    return render(request, 'HOD/update_Cat.html', context)
@login_required()
def Update_cat(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        category_id = request.POST.get('category_id')
        print(category)
        print(category_id)

    
        cat = Catagory.objects.get(id=category_id)
        cat.catagory_name = category
        messages.success(request, 'Category Successfully Updated!')
        cat.save()
        return redirect('Pharmacey_App:View_Category')
    messages.error(request, 'Update Faild!')
    return redirect('Pharmacey_App:Update_cat')

@login_required()
def Delete_Cat(request, id):
    Cat = Catagory.objects.get(id=id)
    Cat.delete()
    messages.success(request,'Category Successfully deleted!')
    return redirect('Pharmacey_App:View_Category')

@login_required()
def Stock_View(request):
    medisince = Stock_Medisice.objects.all()
    context = {
        'medisince':medisince,
    }
    return render(request, 'HOD/stock_view.html', context)

@login_required()
def Add_Stock(request):
    category = Catagory.objects.all()
    supplier = Suplier.objects.all()
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        catagory = request.POST.get('catagory')
        supplier = request.POST.get('supplier')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        expire_date = request.POST.get('expire_date')
        medicine_image = request.FILES.get('medicine_image')

        if expire_date is None:
            messages.warning(request, 'Expired Date Must Be Set!')
            return redirect('Pharmacey_App:Add_Stock')

        catagory = Catagory.objects.get(id=catagory)
        supplier = Suplier.objects.get(id=supplier)
        Add_Stock = Stock_Medisice(
            medicine_name = medicine_name,
            Category = catagory,
            Supplier = supplier,
            price = price,
            quatity = quantity,
            exire_date = expire_date,
            medicine_img = medicine_image,
        )
        Add_Stock.save()
        messages.success(request, 'Stock Successfully Added!')
        return redirect('Pharmacey_App:Add_Stock')


    context = {
        "category":category,
        'supplier':supplier,
    }
    
    return render(request, 'HOD/add_stock.html', context)
@login_required()
def Edit_stock(request, id):
    stock_medicine = Stock_Medisice.objects.get(id=id)
    category = Catagory.objects.all()
    supplier = Suplier.objects.all()
    context = {
        'stock_medicine':stock_medicine,
        'category':category,
        'supplier':supplier
    }
    return render(request, 'HOD/update_stock.html', context)
@login_required()
def Update_Stock(request):
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        catagory = request.POST.get('catagory')
        supplier = request.POST.get('supplier')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        expire_date = request.POST.get('expire_date')
        medicine_image = request.FILES.get('medicine_image')
        stock_id = request.POST.get('stock_id')

        catagory = Catagory.objects.get(id=catagory)
        supplier = Suplier.objects.get(id=supplier)

        stock = Stock_Medisice.objects.get(id=stock_id)
        stock.medicine_name = medicine_name
        if expire_date == '':
            messages.warning(request, 'Update Fail! Expired Date Must Be Set.')
            return redirect('Pharmacey_App:Stock_View')
        if catagory is not None:
            stock.Category = catagory
        if supplier is not None:
            stock.Supplier = supplier
        
        if medicine_image is not None:
            stock.medicine_img = medicine_image
        
        stock.price = price
        stock.quatity = quantity
        stock.exire_date = expire_date
        stock.save()
        messages.success(request, 'Stock Successfully Updated!')
        return redirect('Pharmacey_App:Stock_View')

    
@login_required()
def Delete_stock(request, id):
    stock = Stock_Medisice.objects.get(id=id)
    stock.delete()
    messages.success(request, 'Stock Successfully Deleted!')
    return redirect('Pharmacey_App:Stock_View')


@login_required()
def View_Suppplier(request):
    supplier = Suplier.objects.all()
    context = {
        'supplier':supplier
    }
    return render(request, 'HOD/view_supp.html', context)

@login_required()
def Add_Suppplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        company = request.POST.get('company')
        product = request.POST.get('product')
        address = request.POST.get('address')
        description = request.POST.get('description')
        supplier = Suplier(
            name = name,
            email = email,
            phone = phone,
            company = company,
            address = address,
            product = product,
            description = description
        )
        supplier.save()
        messages.success(request, 'Suplier Added Successfully!')
        return redirect('Pharmacey_App:Add_Suppplier')
    return render(request, 'HOD/add_supplier.html')


@login_required()
def Edit_Suplier(request, id):
    suplier = Suplier.objects.get(id=id)

    context = {
       'suplier':suplier 
    }

    return render(request, 'HOD/edit_suplier.html', context)

@login_required()
def Update_Suppplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        company = request.POST.get('company')
        product = request.POST.get('product')
        address = request.POST.get('address')
        description = request.POST.get('description')
        suplier_id = request.POST.get('suplier_id')
         
        suplier = Suplier.objects.get(id=suplier_id)

        suplier.name = name
        suplier.email = email
        suplier.phone = phone
        suplier.company = company
        suplier.address = address
        suplier.product = product
        suplier.description = description
        suplier.save()
        messages.success(request, 'Suplier Successfully Updated!')
        return redirect ('Pharmacey_App:View_Suppplier')
    return None



@login_required()
def Delete_Suppplier(request, id):
    suplier = Suplier.objects.get(id=id)
    suplier.delete()
    messages.success(request, 'Suplier Successfully Deleted!')
    return redirect('Pharmacey_App:View_Suppplier')


@login_required()
def View_medicine(request):
    medicine = Medicine.objects.all()
    context = {
        'medicine':medicine
    }
    return render(request, 'HOD/view_medicine.html', context)


@login_required()
def View_Client(request):
    client = Client.objects.all()
    context = {
        'client':client
    }
    return render(request, 'HOD/view_client.html', context)


@login_required()
def Add_Client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        company = request.POST.get('company')
        product = request.POST.get('product')
        address = request.POST.get('address')
        description = request.POST.get('description')
        client = Client(
            name = name,
            email = email,
            phone = phone,
            company = company,
            address = address,
            product = product,
            description = description
        )
        client.save()
        messages.success(request, 'Client Added Successfully!')
        return redirect('Pharmacey_App:add_client')
    return render(request, 'HOD/add_client.html')


@login_required()
def Edit_Client(request, id):
    client = Client.objects.get(id=id)

    context = {
       'client':client 
    }

    return render(request, 'HOD/edit_client.html', context)


@login_required()
def Update_Client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        company = request.POST.get('company')
        product = request.POST.get('product')
        address = request.POST.get('address')
        description = request.POST.get('description')
        suplier_id = request.POST.get('suplier_id')
         
        client = Client.objects.get(id=suplier_id)

        client.name = name
        client.email = email
        client.phone = phone
        client.company = company
        client.address = address
        client.product = product
        client.description = description
        client.save()
        messages.success(request, 'Client Successfully Updated!')
        return redirect ('Pharmacey_App:view_client')
    return None

@login_required()
def Delete_Client(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    messages.success(request, 'Client Successfully Deleted!')
    return redirect('Pharmacey_App:view_client')


@login_required()
def Add_Medicine(request):
    stock = Stock_Medisice.objects.all()
    if request.method == 'POST':
        medicine_id = request.POST.get('medicine_id')
        selling_price = request.POST.get('selling_price')
        discount = request.POST.get('discount')
        description = request.POST.get('description')

        stock = Stock_Medisice.objects.get(id=medicine_id)
        if Medicine.objects.filter(id=medicine_id).exists():
            messages.warning(request, 'This Medisine Already Exists!')
            return redirect('Pharmacey_App:add_medicine')
        else:
            medicine = Medicine (
                medicine = stock,
                selling_Price = selling_price,
                discount = discount,
                Description = description,
            )
            medicine.save()
            messages.success(request, 'Medicine Suceessfully added!')
            return redirect('Pharmacey_App:add_medicine')
        


    context = {
       'stock':stock 
    }
    return render(request, 'HOD/add_medicine.html', context)



@login_required()
def Edit_Medicine(request, id):
    medicine = Medicine.objects.get(id=id)
    stock = Stock_Medisice.objects.all()

    context = {
       'stock':stock,
       'medicine':medicine
    }
    return render(request, 'HOD/edit_medicine.html', context)


@login_required()
def Update_Medicine(request):
    if request.method == 'POST':
        medicine_id = request.POST.get('medicine_id')
        selling_price = request.POST.get('selling_price')
        discount = request.POST.get('discount')
        description = request.POST.get('description')
        medicine_id2 = request.POST.get('medicine_id2')
        stock = Stock_Medisice.objects.get(id=medicine_id)

        medicine = Medicine.objects.get(id=medicine_id2)

        medicine.medicine = stock
        medicine.selling_Price = selling_price
        medicine.discount = discount
        medicine.Description = description
        medicine.save()
        messages.success(request, 'Medicine Successfully Updated!')
        return redirect('Pharmacey_App:view_medicine')
    return None


@login_required()
def View_Sale(request):
    sale = Sale.objects.all()
    context = {
        'sale':sale
    }
    return render(request, 'HOD/view_sale.html', context)



@login_required()
def Add_Sale(request):
    medicinee = None
    medicine = Medicine.objects.all()
    client = Client.objects.all()
    if request.method == 'POST':
        medicine_id = request.POST.get('medicine_id')
        client_id = request.POST.get('client_id')
        quantity = request.POST.get('quantity')
        medicinee = Medicine.objects.get(medicine=medicine_id)
        client = Client.objects.get(id=client_id)
        main_quantity = medicinee.medicine.quatity
        if main_quantity is not None:
            quantity2 = int(quantity)
            totall_quantity = float(main_quantity-quantity2)
            if totall_quantity >= 0:
                stock = Stock_Medisice.objects.get(id=medicine_id)
                stock.quatity = totall_quantity
                stock.save()
            else:
                messages.warning(request, 'You have not enough stock!')
                return redirect('Pharmacey_App:Stock_View')
        else:
            messages.warning(request, 'Your Product quintity 0!')
            return redirect('Pharmacey_App:Stock_View')
            
        
        # for i in medicinee:
        #     result = i.medicine.id
        #     print('---------------Print------------')
        #     print(result)
        sale = Sale(Product=medicinee, quntity=quantity, client=client)
        sale.save()
        messages.success(request, 'Sale Successfully Confirmed!')
        return redirect('Pharmacey_App:view_sale')
    
        
        
    context = {
        'medicine':medicine,
        'client':client
    }


    return render(request, 'HOD/add_sale.html', context )

def Sale_delete(request, id):
    sale = Sale.objects.get(id=id)
    sale.delete()
    messages.success(request, 'Sale Successfully Deleted!')
    return redirect('Pharmacey_App:view_sale')

def Stock_out(request):
    Stock_out = Stock_Medisice.objects.filter(quatity=0)
    
    context = {
        'Stock_out':Stock_out
    }
    return render(request, 'HOD/stock_out.html', context)

def Expired_medicine(request):
    Stock_out = Stock_Medisice.objects.filter(quatity=0)
    context = {

    }
    return render(request, 'HOD/expired_list.html', context)


