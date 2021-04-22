# from django.conf.urls import url 
from django.urls import path
from myapp import views 
from django.contrib import admin
 
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('entertainment/', views.Fetchbytypeentertainment, name='entertainment'),
    path('learning/', views.Fetchbytypelearning, name='learning'),
    path('disabledandelderly/', views.Fetchbytypedisabledandelderly, name='disabledandelderly'),
    path('scienceadntecnology/', views.Fetchbytypescienceadntecnology, name='scienceadntecnology'),
    path('mobileapplication/', views.Fetchbytypemobileapplication, name='mobileapplication'),
    path('2563/',views.Fetchbyyear, name='2563'),
    path('data0266/',views.detail, name='detail'),
    path('all/', views.dataAll, name='dataall'),
    path('search/', views.search, name='search'),
    path('',views.index, name='index'),

]