
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('create/', views.create,name="create"),
    path('delete/<Faturalar_id>', views.delete,name="delete"),
    path('yes_finish/<Faturalar_id>', views.yes_finish,name="yes_finish"),
    path('no_finish/<Faturalar_id>', views.no_finish,name="no_finish"),
    path('update/<Faturalar_id>', views.update,name="update"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name= "logout"),
    path('users/', views.users,name="users"),
]
