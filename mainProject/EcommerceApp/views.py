from django.shortcuts import render, redirect

from django.contrib.auth import login
from .form import RegistrationForm

from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Product,Order,OrderItem

from django.http import HttpResponse

import json

# Create your views here.
def store(request):


    products =   Product.objects.all()

    context = {

        'products':products
    }


    return render(request,  'ecomm/store.html', context)



def cart(request):
    
    return render(request, 'ecomm/cart.html' )


import json
from django.http import JsonResponse

def updateCart(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid or empty JSON"}, status=400)

        productId = data.get('productId')
     

        print("Product:", productId)

        product = Product.objects.get(id=productId)

    if request.user.is_authenticated:
        

        order, created = Order.objects.get_or_create(user=request.user,complete = False)

        orderItems, created = OrderItem.objects.get_or_create(order = order,product =product)

        orderItems.quantity += 1

        orderItems.save()
        return JsonResponse({"message": "Item updated!"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)












def updateCart(request):

    data = json.loads(request.body)

    product_id = data[product_id]

    



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