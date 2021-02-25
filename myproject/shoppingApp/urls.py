from django.urls import path

from .views import welcome, get_all_items,delete_items

urlpatterns = [
    path('welcome/<str:name>',welcome),
    path('get_all_items/',get_all_items),
    path('delete_items/<str:name>',delete_items)

]

