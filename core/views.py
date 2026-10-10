from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Read (List)
def product_list(request):
  products = Product.objects.all()
  return render(request, 'products/item_list.html', {'products': products})


# Create
def product_create(request):
  error = None
  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')

    if name:
      Product.objects.create(name=name, description=description)
      return redirect('product_list')
    else:
      error = 'Name field is required.'

  return render(request, 'products/item_form.html', {'error': error})

# Update
def product_update(request, pk):
  product = get_object_or_404(Product, pk=pk)
  error = None

  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')

    if name:
      product.name = name
      product.description = description
      product.save()
      return redirect('product_list')
    else:
      error = 'Name field is required.'

  return render(request, 'products/item_form.html', {'product': product, 'error': error})

def product_delete(request, pk):
  product = get_object_or_404(Product, pk=pk)
  if request.method == 'POST':
    product.delete()
    return redirect('product_list')
  return render(request, 'products/item_confirm_delete.html', {'product': product})