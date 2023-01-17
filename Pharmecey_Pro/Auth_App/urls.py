from django.urls import path
from . import views

app_name = 'Auth_app'

urlpatterns = [
    path('login/', views.User_Login, name='login'),
    path('logout/', views.User_Logout, name='logout'),
    path('user-profile/<id>/', views.User_Profile, name='userprofile'),
    path('edit-profile/', views.Edit_Profile, name='edit_profile'),
    path('update-profile/', views.Update_profile, name='update_profile'),
    path('change-password/', views.Change_password, name='change_password')
]
