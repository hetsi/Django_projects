from django.urls import path
from .views import greeting, get_time,add_nums,adding_by_get

urlpatterns = [
    path('greeting/',greeting),
    path('get_time/',get_time),
    path('solve/',adding_by_get),
    path('<int:num1>/<int:num2>/',add_nums)

]