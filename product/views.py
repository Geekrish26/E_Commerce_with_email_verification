from django.shortcuts import render
from product.models import Product
from pydoc import render_doc
from tkinter import E
from accounts.models import Cart , CartItems , SizeVariant
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.


def get_product(request , slug):
    try:
        product=Product.objects.get(slug = slug)
        context = {'product' : product}
        if request.GET.get('size'):
            size= request.GET.get('size')
            price=product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price

        return render(request , 'product/product.html', context = context)
    
    except Exception as e:
        return HttpResponse("An error occurred while processing the request.", status=500)



# def add_to_cart(request , uid):
#     variant = request.Get.get('variant')
#     product= Product.objects.get(uid=uid)
#     user = request.user
#     cart, _ = Cart.objectsget_or_create(user = user , is_paid = False)
#     cart_items = CartItems.objects.create(cart= cart , product=product)

#     if variant:
#         variant= request.GET.get('variant')
#         size_variant = SizeVariant.objects.get(size_name = variant)
#         cart_items.size_variant = size_variant
#         cart_items.save()

#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))