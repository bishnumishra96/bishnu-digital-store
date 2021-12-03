from django.core import paginator
from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import activate
from django.views import View
from django.views.generic import FormView
from store.models import Category, Product
from django.views.generic import ListView
from django.core.paginator import Paginator
# Create your views here.



class HomeView(ListView):
    model  = Product
    template_name = 'store/index.html'
    context_object_name = 'products'
    paginate_by = 2
    def get_context_data(self):
        page = self.request.GET.get('page')
        if page is None:
            page = 1
        category_pk = self.request.GET.get("category")
        categories = Category.objects.all()
        if category_pk:
            products = Product.objects.filter(category= category_pk,active = True)
            # category_pk = int(category_pk)
        else:
            products = Product.objects.filter(active = True)
        
        paginator = Paginator(products , self.paginate_by)
        context = {
            'categories': categories,
            'page_obj':paginator.page(page)
            #'products':products,
            # 'active_category':category_pk,
             }
        return context






'''

class Home_View(View):
    def get(self, request):
        products  = Product.objects.all()
        context = {
            'products':products
        }
        return render(request,template_name='store/index.html',context=context)


'''

'''
def home(request):
    products  = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,template_name='store/index.html',context=context)
'''


def about(request):    
    return HttpResponse('Hello about')
def contactus(request):
    return HttpResponse('Hello contactus')