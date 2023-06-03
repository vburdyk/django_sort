from django.shortcuts import render
from .models import Category, Product


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    sort_by = request.POST.get("sort_by")
    products = category.products.all()

    if sort_by == 'price low-high':
        products = products.order_by('price')
        return render(request, 'category.html', {"category": category, "products": products})

    if sort_by == 'price high-low':
        products = products.order_by('-price')
        return render(request, 'category.html', {"category": category, "products": products})

    if sort_by == 'date high-low':
        products = products.order_by('created_at')
        return render(request, 'category.html', {"category": category, "products": products})

    if sort_by == 'date low-high':
        products = products.order_by('-created_at')
        return render(request, 'category.html', {"category": category, "products": products})

    else:
        return render(request, 'category.html', {"category": category, "products": products})
