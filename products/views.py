from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        is_active=True
    )

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product
        }
    )