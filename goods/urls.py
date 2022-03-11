import imp
from django.urls import path
from .views import *

urlpatterns = [
    # path('', index),
    path('', GoodsView.as_view(), name='goods'),
    path('products/', products, name='sorting'),
    path('product/', product, name="product")
]
