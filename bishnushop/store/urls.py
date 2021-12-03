
from django.contrib import admin
from django.urls import path,include
from .views.auth import SignupView , LoginView,logout_view #signup_view
from .views.home import  HomeView,about,contactus #home
from .views.details import ProductDetailView #product_detail_view
from .views.checkout import checkout
from .views.payment import create_payment,payment_verify,download_file
from .views.order import OrderListView



urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',about),
    path('contactus',contactus),
    path('logout',logout_view,name='logout'),
    #path('signup',signup_view),
    path('signup',SignupView.as_view()),
    path('login',LoginView.as_view(), name='login'),
    #path('product/<str:slug>/',product_detail_view),
    path('product/<str:slug>/',ProductDetailView.as_view()),
    path('checkout/<str:slug>',checkout, name='checkout' ),
    path('payment/verify',payment_verify, name= 'verify_payment'),
    path('payment/<str:slug>',create_payment, name= 'create_payment'),
    path('orders/',OrderListView.as_view(), name = 'orders'),
    path('download/<str:slug>',download_file, name = 'download')
    

]
