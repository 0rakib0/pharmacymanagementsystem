from django.urls import path
from Pharmacey_App import views

app_name  = "Pharmacey_App"

urlpatterns = [
    # -------------------> main / HOD urls <==----------------- 
    path('', views.Deshbord, name='Deshbord'),

    # ---------------> Catagory ulrs <--------------------------
    path('add-category/', views.Add_Category,name='Add_Category'),
    path('view-category/', views.View_Category,name='View_Category'),
    path('Edit-category/<str:id>/', views.Edit_Cat,name='Edit_Cat'),
    path('update-category/', views.Update_cat,name='Update_cat'),
    path('delete-category/<id>/', views.Delete_Cat,name='Delete_Cat'),
    # ---------------> Stock Purchase ulrs <--------------------------
    path('stock-view/', views.Stock_View, name='Stock_View'),
    path('add-stock-purchese/', views.Add_Stock, name='Add_Stock'),
    path('Edit-stock/<id>/', views.Edit_stock, name='Edit_stock'),
    path('update-stock/',views.Update_Stock, name='update_stock' ),
    path('delete-stock/<id>/', views.Delete_stock, name='delete_stock'),

    # ---------------> Supplier ulrs <--------------------------
    path('view-suplier/', views.View_Suppplier, name='View_Suppplier'),
    path('add-suplier/', views.Add_Suppplier, name='Add_Suppplier'),
    path('edit-suplier/<id>/', views.Edit_Suplier, name='edit_suplier'),
    path('update-suplier/', views.Update_Suppplier, name='Update_Suppplier'),
    path('delete-suplier/<id>/', views.Delete_Suppplier, name='Delete_Suppplier'),

    # ---------------> Client ulrs <--------------------------
    path('add-client/', views.Add_Client, name='add_client'),
    path("view-client/", views.View_Client, name="view_client"),
    path("edit_client/<id>/", views.Edit_Client, name="edit_client"),
    path("update-client/", views.Update_Client, name="update_client"),
    path("delete-client/<id>/", views.Delete_Client, name="delete_client"),

    # ---------------> Medicine ulrs <--------------------------
    path('view-medicine/', views.View_medicine, name='view_medicine'),
    path('add-medicine/', views.Add_Medicine, name='add_medicine'),
    path('edit-medicine/<id>/',views.Edit_Medicine, name='edit_medicine' ),
    path('update-medicine/', views.Update_Medicine, name='update_medicine'),
    path('stock-out/',views.Stock_out, name='stock_out' ),

    # ---------------> Medicine ulrs <--------------------------
    path('view-sale/', views.View_Sale, name='view_sale'),
    path('add-sale/', views.Add_Sale, name='add_sale'),
    path('Delete-sale/<id>/', views.Sale_delete, name='sale_delete'),

]
