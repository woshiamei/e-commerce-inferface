"""InferfaceProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.views import get_sim_products
from myapp.views import Login, AddData, SetData, GetData
from myapp.views_user import CacheTest, CacheSet, CacheGet, SetUserTop, GetUserTop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login),
    path('add_data/', AddData),
    path('set_data/', SetData),
    # path('get_data/', GetData),
    path('get_product_sim/', GetData),
    path('cache_test/', CacheTest),
    path('cache_set/', CacheSet),
    path('cache_get/', CacheGet),
    path('user_reco/set_user_top/', SetUserTop),
    path('user_reco/get_user_top/', GetUserTop)
]
