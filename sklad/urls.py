from django.urls import path
from . import views

urlpatterns = [

    path('register', views.register, name="register"),

    path('', views.login, name="login"),

    path('logout', views.logout, name="logout"),

    path('create_iteam', views.createIteam, name="create_iteam"),

    path('view_iteam', views.viewIteam, name="view_iteam"),

    path('update_iteam/<str:pk>/', views.updateIteam, name="update_iteam"),

    path('delete_iteam/<str:pk>/', views.deleteIteam, name="delete_iteam"),

]
