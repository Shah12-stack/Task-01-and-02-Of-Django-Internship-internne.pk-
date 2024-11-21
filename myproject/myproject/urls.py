from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('introduce/', include('introduction.urls')),  
    path('', lambda request: redirect('introduce/')),


]
