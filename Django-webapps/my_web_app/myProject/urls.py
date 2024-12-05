from django.urls import path

from . import views
urlpatterns =[
    path('create/',views.create_view),
    path('list/',views.list_view),
    path('detail/<id>',views.detail_view),
    path('update/<id>',views.update_view),
    path('delete/<id>',views.delete_view),
    path('products/',views.create_product),
    path('products_list/',views.list_product),
    path('product_detail/<id>',views.product_detail),
    path('product_update/<id>',views.update_product),
    path("product_delete/<id>",views.delete_product),
]

