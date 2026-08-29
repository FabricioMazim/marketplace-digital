from django.shortcuts import render
from products.models import Product


def home(request):
    products = Product.objects.filter(is_active=True).order_by("-created_at")[:6]

    return render(
        request,
        "core/home.html",
        {
            "products": products
        }
    )