
from django.contrib import admin
from django.urls import path,include
from .settings import MEDIA_ROOT,MEDIA_URL
from django.conf import settings
from django.conf.urls.static import static
# from store.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
] + static(MEDIA_URL, document_root=settings.MEDIA_ROOT)
