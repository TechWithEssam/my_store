from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .forms import UserAccountForm
from django.contrib import messages
from store.models import Product, Sales
from store.forms import AddNewProductForm  
from django.http import HttpResponse

@login_required
def account_sales_view(request) :
    template_name = "accounts/my-account.html"
    profile = Profile.objects.get(user=request.user)
    if profile.is_buyer == True :
        qs = Account.objects.get(buyer=profile)
    else :
        raise Http404
    context = {
        "obj" : qs
    }
    return render(request, template_name, context)

@login_required
def detail_account_buyer_view(request, **kwargs) :
    template_name = "accounts/account-buyer.html"
    url = kwargs.get("url")
    if url is not None :
        try :
            qs = Account.objects.get(url=url)
        except :
            return JsonResponse({"masg": "this account is not found"})

    context = {
        "qs":qs,
        "profile": Profile.objects.get(user=request.user)
        }
    return render(request, template_name, context)


@login_required
def action_follow_unfollow_view(request) :
    if request.method == "POST" :
        account_id = request.POST.get("account_id")
        profile = Profile.objects.get(user=request.user)
        if account_id is not None :
            account = Account.objects.get(pk=account_id)
            obj = account
            if profile in obj.followers.all() :
                obj.followers.remove(profile)
            else :
                obj.followers.add(profile)
                obj.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def create_account_view(request) :
    template_name = 'accounts/create_account.html'
    profile = Profile.objects.get(user=request.user)
    form = UserAccountForm(request.POST or None, request.FILES or None)
    if form.is_valid() :
        instance = form.save(commit=False)
        instance.buyer = profile
        instance.save()
        return redirect("accounts:my_account")
    context = {
        "profile":profile,
        "form" : form
    }
    return render(request, template_name, context)

@login_required
def update_information_your_account(request) :
    template_name = 'accounts/create_account.html'
    profile = request.user.profile
    buyer = Account.objects.get(buyer=profile)
    form = UserAccountForm(request.POST or None, request.FILES or None, instance=buyer)
    if form.is_valid() :
        form.save()
        return redirect("accounts:my_account")
    context = {
        "buyer":buyer,
        "u_form" : form
    }
    return render(request, template_name, context)

@login_required
def delete_my_account_view(request, **kwargs) :
    template_name = 'accounts/create_account.html'
    pk = kwargs["pk"]
    profile = request.user.profile
    account = Account.objects.get(pk=pk)
    if request.method == "POST" :
        if profile == account.buyer :
            account.delete()
            return redirect("users:my_profile")
        else :
            messages.error(request, "you dont have permission to delete this account")
    context = {
        "account":account
    }
    return render(request, template_name, context) 
        

@login_required
def update_my_product_view(request, slug) :
    template_name = 'store/create-update.html'
    profile = request.user.profile
    salesman = Account.objects.get(buyer=profile)
    product = Product.objects.get(slug=slug)
    form = AddNewProductForm(request.POST or None,request.FILES or None, instance=product)
    if form.is_valid() :
        if salesman == product.salesman :
            form.save()
            return redirect(product.detail_product_url)
        else :
            return JsonResponse({"masg":"this product not for you "})
    context = {
        "u_form":form
    }
    return render(request, template_name, context)

@login_required
def delete_product_view(request, slug) :
    template_name = "store/create-update.html"
    product = Product.objects.get(slug=slug)
    if request.method == "POST" :
        product.delete()
        return redirect("accounts:my_account")
    context = {
        "product":product
    }
    return render(request, template_name, context)

@login_required
def my_orders_view(request, done=None) :
    templates_name = "accounts/all_orders.html"
    profile = request.user.profile
    if profile.is_buyer == True :
        account = Account.objects.get(buyer=profile)
        if done == None :
            try :
                all_orders = Sales.objects.filter(product__salesman=account).order_by("-timestamp")
            except :
                return HttpResponse("you are not have a sales")
        elif done == "done" :
            all_orders = Sales.objects.filter(product__salesman=account, status="sdh").order_by("-timestamp")
        else :
            return HttpResponse("you are not have a sales")
    else :
        return redirect("accounts:create_account")
    context = {
        "all_orders":all_orders,
        "buyer":account
    }
    return render(request, templates_name, context)


@login_required
def detail_order_view(request, pk) :
    template_name = "accounts/detail-order.html"
    profile = request.user.profile
    if profile.is_buyer == True :
        try :
            obj = Sales.objects.get(pk=pk)
        except :
            obj = None
    else :
        return redirect("accounts:create_account")
    context = {
        "obj":obj
    }
    return render(request, template_name, context)

