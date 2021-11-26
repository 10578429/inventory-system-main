from django.shortcuts import render
from .forms import ProductForm
from .models import Product


# Create your views here.
def all_products_view(request):
    context = {
        "products": get_all_products(),
        "products_by_categories": get_products_by_category()
    }

    return render(request, 'inventory/products.html', context)


def get_all_products():

    products = []
    products_obj = Product.objects.all()

    for product in products_obj:

        products.append({
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "category": product.category,
            "available": product.available,
            "image": product.image
        })

    return products


def get_products_by_category():

    products_obj = Product.objects.all()

    categories = {}
    for product in products_obj:

        category = product.get_category_display()
        if category is not None and category not in categories.keys():
            categories[category] = []

        categories[category].append(
            {
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "category": product.category,
                "available": product.available,
                "image": product.image
            }
        )

    for cat, products in categories.items():
        if len(products) > 4:
            categories[cat] = [products[each: each + 4] for each in range(0, len(products), 4)]
        else:
            categories[cat] = [products]

    print(categories)
    return categories


def add_new_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, 'inventory/new_product.html', context)
