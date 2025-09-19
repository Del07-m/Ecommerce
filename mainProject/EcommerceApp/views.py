from django.shortcuts import render, redirect

from django.contrib.auth import login
from .form import RegistrationForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Product,Order,OrderItem

from django.http import HttpResponse

import json

# Create your views here.
def store(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        cartItems = sum(item.quantity for item in order.orderitem_set.all())
    else:
        cartItems = 0

    context = {
        'products': products,
        'cartItems': cartItems
    }
    return render(request, 'ecomm/store.html', context)


def cart(request):
    
    
    return render(request, 'ecomm/cart.html' )




def updateCart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        # get or create order
        order, created = Order.objects.get_or_create(user=request.user, complete=False)

        # get or create order item
        cartitem, created = OrderItem.objects.get_or_create(order=order, product=product)

        # increment quantity
        cartitem.quantity += 1
        cartitem.save()

        cart_items = sum(item.quantity for item in order.orderitem_set.all())
    else:
        cart_items = 0  # for guests

    return JsonResponse({
    "message": "Its working",
    "status": "success",
    "cartItems": cart_items
})














    



    # return HttpResponse("its working and has been posted")



def register(request):

    if request.method == "POST":
           form = RegistrationForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, "Account created successfully! You can now log in.")
               return redirect("login")
           else:
            print(form.errors)  # 👈 DEBUG: show errors in terminal
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegistrationForm()

    return render(request, "ecomm/signup.html", {"form": form})
# END OF SIGNUP LOGIC 

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  
        else:
            messages.info(request, 'username OR password is incorrect')
    context = {}       
    return render(request, 'ecomm/login.html', context)