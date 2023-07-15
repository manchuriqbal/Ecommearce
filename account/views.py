from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect,  HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from product.models import SizeVarient, Product
from .models import Cart, CartItams


def login_page(request):
     
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_obj = User.objects.filter(username = email)
    
        if not user_obj.exists():
            messages.warning(request, "Account not found.")
            return HttpResponseRedirect(request.path_info)
    
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "This is email is not verified.")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect("/")

        messages.success(request, "Invalid credentials.")
        return HttpResponseRedirect(request.path_info)
    
    return render(request, "accounts/login.html")
    


def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request, "This email is alrady taken.")
            return HttpResponseRedirect(request.path_info)
            
        
        user_obj = User.objects.create(first_name=first_name, last_name= last_name, username = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "email send on your email.")
        return HttpResponseRedirect(request.path_info)

    return render(request, "accounts/register.html")


def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect("/")

    except Exception as e:
        return HttpResponse('Invalid Email token')



def add_to_cart(request, uid):
    varient = request.GET.get("varient")
    product = Product.objects.get(uid=uid)
    user = request.user
    (cart, _) = Cart.objects.get_or_create(user=user, is_paid = False)

    cart_item = CartItams.objects.create(cart = cart, product = product)

    if varient:
        varient = request.GET.get("varient")
        size_varient = SizeVarient.objects.get(size_name = varient)
        cart_item.size_varient = size_varient
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def cart(request):
    cart_items = CartItams.objects.filter(cart__is_paid=False, cart__user=request.user)
    context = {"cart": cart_items}
    return render(request, "accounts/cart.html", context)



def delete_cart(request, uid):
    try:
        cart_item = CartItams.objects.get(uid=uid)
        cart_item.delete()
    except Exception as e:
        print(e)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



