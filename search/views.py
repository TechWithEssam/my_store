from django.shortcuts import render
from store.models import Product
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def search_product_view(request) :
    template_name = "search/search.html"
    if request.method == "GET" :
        q = request.GET.get("q")
        qs = Product.objects.search(q)
        is_empty = False 
        if len(qs) == 0 :
            is_empty = True
    context = {
        "qs" : qs,
        'is_empty' : is_empty
    }
    return render(request, template_name, context)