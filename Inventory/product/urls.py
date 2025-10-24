from django.urls import path
from .views import add_products,list_product,update_product,delete_product,all_inventory,category


urlpatterns=[
    path('product/new/',add_products.as_view(),name='newproduct'),
    path('product/list/',list_product.as_view(),name='productlist'),
    path('product/update/',update_product.as_view(),name='productupdate'),
    path('product/delete/',delete_product.as_view(),name='productdelete'),
    path('product/listquantity/',all_inventory.as_view(),name='listquantity'),
    path('product/filtercategory/',category.as_view,name='category'),
    
    ]
