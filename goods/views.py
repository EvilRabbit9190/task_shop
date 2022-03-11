from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Good

def products(request):
    category = request.GET.get("sort")
    goods = Good.objects.all()
    if category == "high_to_low":
        return render(request, "catalog/index.html", context={
            "goods": goods.order_by("-cost")
        })
    elif category == "low_to_high":
        return render(request, "catalog/index.html", context={
            "goods": goods.order_by("cost")
        })
    elif category == "popular":
        return render(request, "catalog/index.html", context={
            "goods": goods.order_by("-raiting")
        })
    else:
        return redirect("/")


def product(request):
    product_id = request.GET.get("id")
    print('product_id: ', product_id)
    product = Good.objects.get(pk=product_id)
    return render(request, "product/index.html", context={
        "product": product
    })
    

class GoodsView(ListView):
    model = Good
    slug_field = 'goods'
    context_object_name = 'goods'
    queryset = Good.objects.all()
    template_name = "catalog/index.html"
