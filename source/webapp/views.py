from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductForm
from webapp.models import Product, CATEGORY_CHOICES


def index_view(request):
    products = Product.objects.filter(amount__gt=1).order_by('category','name')
    return render(request, 'index.html', context={
        'products': products
    })

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })

def product_create_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'create.html', context={
            'category_choices': CATEGORY_CHOICES, 'form': form
        })
    elif request.method == 'POST':
            form = ProductForm(data=request.POST)
            if form.is_valid():
                product = Product.objects.create( name= form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                category = form.cleaned_data['category'], amount = form.cleaned_data['amount'],
                price = form.cleaned_data['price'])
                return redirect('task_view', pk=product.pk)

            else:
                return render(request, 'create.html', context={'category_choices': CATEGORY_CHOICES, 'form': form})

def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'amount': product.amount,
            'price': product.price
        })
        return render(request, 'update.html', context={'form':form, 'product': product, 'category_choises': CATEGORY_CHOICES})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.amount = form.cleaned_data['amount']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'product': product, 'category_choices': CATEGORY_CHOICES})

# def task_delete_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'delete.html', context={'product': product})
#     elif request.method == 'POST':
#         product.delete()
#         return  redirect('index')
