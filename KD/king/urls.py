from django.conf.urls import url, include
from king import views
from django.urls import path, re_path

app_name = 'king'

urlpatterns = [
    path('',views.index,name="index"),
    path('header/',views.header,name="header"),
    path('login1/',views.form_view,name="login"),
    path('product_list/',views.product_list,name="product_list"),
    path('product_list/product_page/<slug:product_name_slug>', views.product_page, name="product_page"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name="user_logout"),
    path('special/',views.special,name="special")
]
