from tree_menu.views import *
from django.urls import path

urlpatterns = [
    path('', menu, name='menu'),

    # Отображаем в адресной строке активные пункты меню
    path('<str:what_menu>/<str:planet>', menu, name='planet'),

]