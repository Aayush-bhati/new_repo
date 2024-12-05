from django.urls import path
from . import views

urlpatterns = [ 
    path('create/',views.create_task),
    path('list/',views.home),
    path('detail/<id>',views.home_details),
    path('update/<id>',views.update_task),
    path('delete/<id>',views.delete_task),
]