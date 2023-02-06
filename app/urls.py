from django.urls import path, include
from app import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='main'),
    path('create-notation/', views.create_notation, name='create_notation'),
    path('delete/<int:id>/', views.delete_notation, name='delete_notation'),
    path('update/<int:id>/', views.update_notation, name='update_notation'),
]
