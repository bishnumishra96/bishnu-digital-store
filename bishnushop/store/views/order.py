from os import terminal_size
from django.db import models
from django.shortcuts import render, redirect
from store.models import UserProduct
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='/login') , name = 'dispatch')
class OrderListView(ListView):
    template_name= 'store/order.html'
    context_object_name = 'orders'
    def get_queryset(self):
        user  = self.request.user
        return UserProduct.objects.filter(user = user).order_by('-payment__date')


#@login_required( login_url='/login')
# def OrderListView(request):
#     # user = None
#     # if request.user.is_authenticated:
#     user  = request.user
#     # else:
#     #     return redirect('login')
#     orders = UserProduct.objects.filter(user = user).order_by('-payment__date')
#     return render(request, template_name='store/order.html',context = {'orders':orders})
