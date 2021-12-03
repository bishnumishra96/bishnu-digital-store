from django.db import models
from django.shortcuts import HttpResponse, render
from store.models import Product
from django.views import View
from django.views.generic import DetailView


class ProductDetailView(DetailView):
    model = Product
    #template_name = 'store/productdetail.html'
    

'''
class ProductDetailView(View):
    def get(self,request , slug):
        product = Product.objects.get(slug = slug)
        context = {
            'product':product
        }
        return render(request, 'store/product_detail.html',context=context)
'''


'''
def product_detail_view(request, slug):
    product = Product.objects.get(slug = slug)
    context = {
        'product':product
    }
    return render(request, 'store/product_detail.html',context=context)
'''