from django.contrib import admin
from django.urls import path,include
from electronics import views
urlpatterns = [
    path('',views.index,name='index'),
    # path('index',views.index,name='index'),

    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('product',views.product,name='product'),
    path('deal',views.deal,name='deal'),
    path('logout/', views.signout, name='signout'),






    # path('About_You',views.About_You,name='About_You')


]