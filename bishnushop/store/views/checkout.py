from django.shortcuts import redirect, render
from store.models import Product
from store.forms import CheckoutForm 
from django.contrib.auth.decorators import login_required
from bishnushop.settings import RAZORPAY_KEY, RAZORPAY_SECRET ,PAYMENT_CALLBACK_URL


@login_required(login_url='/login')
def checkout(request,slug):
    # if request.user.is_authenticated:
    #     user = request.user
    # else:
    #     return redirect('login')
    user = request.user
    form = CheckoutForm(initial={'email': user.email})
    product =   Product.objects.get(slug=slug)
    context = {
        'product':product,
        'form':form,
        'RAZORPAY_KEY':RAZORPAY_KEY,
        'PAYMENT_CALLBACK_URL': PAYMENT_CALLBACK_URL
    }
    return render(request, template_name='store/checkout.html', context=context)
