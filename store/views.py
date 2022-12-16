from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, OrderPlaced
from .forms import *
from users.models import Profile
from accounts.models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.contrib import messages


def home_and_filter_product_view(request, category=None, brand=None, data=None) :
    template_name = "store/home.html"

    if category is  None and brand is None and data is None :
        obj = Product.objects.all()
    elif brand == None and data == None :
        obj = Product.objects.all().filter(category__slug=category).order_by("?")
    elif data == None :
        obj = Product.objects.all().filter(category__slug=category).filter(brand__slug=brand).order_by("?")

    elif data == "below1000" :
        obj = Product.objects.all().filter(price__lte=1000,price__gte=500)

    elif data == "below2000" :
        obj = Product.objects.all().filter(price__lte=2000,price__gte=1000)
    elif data == "below3000" :
        obj = Product.objects.all().filter(price__lte=3000,price__gte=2000)
    elif data == "below4000" :
        obj = Product.objects.all().filter(price__lte=4000,price__gte=3000)

    elif data == 'above5000':
        obj = Product.objects.all().filter(price__lte=7000, price__gte=5000)

    elif data == 'above8000':
        obj = Product.objects.all().filter(price__lte=10000, price__gte=8000)

    elif data == 'above10000':
        obj = Product.objects.all().filter(price__lte=15000, price__gte=10000)

    elif data == 'above15000':
        obj = Product.objects.all().filter(price__lte=25000, price__gte=15000)
    
    else :
        raise Http404

    context={
        "qs":obj
    }
    return render(request, template_name, context)


def detial_product_view(request, **kwargs) :
    template_name = "store/detail.html"
    slug = kwargs.get("slug")
    if slug is not None :
        qs = Product.objects.get(slug=slug)
    context = {
        "qs" : qs
    }
    return render(request, template_name, context)

@login_required
def add_to_cart_view(request) :
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST" :
        product_pk = request.POST["product_pk"]
        product = Product.objects.get(pk=product_pk)
        cart, created = Cart.objects.get_or_create(
            product=product,
            user=profile
        )
        if cart.product.name :
            cart.quantity +=1
            cart.save()
        return redirect(request.META.get('HTTP_REFERER'))
   

@login_required
def minus_product_form_cart_view(request) :
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST" :
        product_pk = request.POST["product_pk"]
        product = Product.objects.get(pk=product_pk)
        cart = Cart.objects.get(product=product, user=profile)
        if cart.product.name :
            cart.quantity -=1
            cart.save()
        if cart.quantity == 0 :
            cart.delete()
    return redirect(request.META.get("HTTP_REFERER"))

@login_required
def cart_user_view(request) :
    template_name = "store/cart.html"
    profile = Profile.objects.get(user=request.user)
    cart = Cart.objects.filter(user=profile)
    total_price = 0 
    total_quantity = 0
    total = 0
    shopping = 0
    for item in cart :
        shopping = 70
        total_price += item.total_cart_price
        total_quantity += item.quantity
        total +=  item.total_cart_price
        

    context = {
        "cart" : cart,
        "total" : total_price,
        'shopping':shopping,
        "total_quantity":total_quantity,
        'amonut' :total + shopping
    }
    return render(request, template_name, context)

@login_required
def remove_product_from_cart(request) :
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST" :
        product_pk = request.POST.get("empty_pk")
        product = get_object_or_404(Product, pk=product_pk)
        item = Cart.objects.filter(Q(product=product) & Q(user=profile))
        item.delete()
    return redirect(request.META.get("HTTP_REFERER"))


@login_required
def order_placed_view(request) :
    template_name = 'store/shopping.html'
    profile = Profile.objects.get(user=request.user)
    cart = Cart.objects.filter(user=profile)
    total_item = 0
    total_price = 0
    shopping = 0.0
    for item in cart :
        shopping = 70
        total_price +=item.total_cart_price
        total_item += item.quantity
        
    if request.method == "POST" :
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        address2 = request.POST.get("address2")
        country = request.POST.get("country")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        if cart is not None :
            for item in cart :
                OrderPlaced.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email = email,
                    address=address,
                    address2=address2,
                    country=country,
                    state=state,
                    zip_code=zip,
                    product=item.product,
                    user=profile,
                    status= "tm",
                    quantity=item.quantity
                ).save()
                cart.delete()
            return redirect("store:my_order")
    context = {
        'cart':cart,
        'total_price':total_price + shopping, 
        "total_item":total_item ,
        'shopping':shopping
    }
    return render(request, template_name, context)

@login_required
def your_order_view(request) :
    template_name = "store/order.html"
    profile = Profile.objects.get(user=request.user)
    obj = OrderPlaced.objects.filter(user=profile).order_by('-timestamp')
    total_orders_price = 0
    shopping = 0
    for item in obj :
        shopping = 70
        total = item.product.new_price_after_dicount * item.quantity
        total_orders_price += total
        if item.status == "sdh" :
            total_orders_price -= item.product.new_price_after_dicount * item.quantity
        if total_orders_price == 0 :
            shopping = 0
    is_empty = False
    if len(obj) > 0 :
        is_empty = True
    context = {
        "is_empty": is_empty,
        "obj" : obj,
        "total":total_orders_price + shopping
    }
    return render(request, template_name, context)


@login_required
def add_new_category_view(request) :
    template_name = "store/create-update.html"
    profile = request.user.profile
    if profile.is_buyer == True :
        created = False
        form = AddNewCategory(request.POST or None)
        if form.is_valid() :
            form.save()
            created = True
    else :
        return JsonResponse({"masg": "you are not buyer can't add category"})
    context = {
        "created" : created,
        "c_form" : form,
    }
    return render(request, template_name, context)
            

@login_required
def add_brand_view(request) :
    template_name = "store/create-update.html"
    profile = request.user.profile
    if profile.is_buyer == True :
        form = AddBrandForm(request.POST or None)
        if form.is_valid() :
            form.save()
            return redirect("store:home")
    else :
        return redirect("accounts:create_account")
    context = {
        "b_form":form
    }
    return render(request, template_name, context)


@login_required
def add_new_product_by_buyer_view(request) :
    template_name = "store/create-update.html"
    profile = request.user.profile
    if profile.is_buyer == True :
        buyer = Account.objects.get(buyer=profile)
        form = AddNewProductForm(request.POST or None, request.FILES or None)
        if form.is_valid() :
            instance = form.save(commit=False)
            instance.salesman = buyer
            instance.save()
            return redirect(instance.detail_product_url)
    else :
        return redirect("accounts:create_account")
    context = {
        "form":form
    }
    return render(request, template_name, context)

        
@login_required
def handed_products_shopping(request) :
    if request.method == "POST" :
        order_pk = request.POST.get("order_pk")
        qs = OrderPlaced.objects.get(pk=order_pk)
        if qs is not None :
            qs.status = 'sdh'
            qs.save()
        return redirect(request.META.get("HTTP_REFERER"))

@login_required
def delete_product_form_orders_view(request, **kwargs) :
    pk = kwargs.get("pk")
    qs = OrderPlaced.objects.get(pk=pk)
    qs.delete()
    return redirect("store:my_order")

@login_required
def empty_orders_be_done_view(request) :
    template_name = "store/empty-orders-be-dane.html"
    profile = request.user.profile
    if request.method == "POST" :
        qs = OrderPlaced.objects.filter(Q(user=profile) & Q(status="sdh"))
        qs.delete()
        return redirect("store:my_order")
    context= {

    }
    return render(request, template_name, context)