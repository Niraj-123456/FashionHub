from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact, name='contact'),
    path('about_us/', views.about, name='about'),
    path('registeruser/', views.register, name='register'),
    path('loginuser/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_account/', views.account, name='account'),
    path('product/', views.product, name='product'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('product/category/<int:cid>', views.category, name='product/category'),
    path('shopping-cart/', views.cart, name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_cart_item/<int:id>', views.delete_item, name='delete_cart_item'),
]