from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='homepage'),
    path("cart",views.cart, name='cart-page'),
    path('register',views.register, name="register"),
    path('login',views.loginPage, name='login'),
    path("updatecart",views.updateCart)
   
]
