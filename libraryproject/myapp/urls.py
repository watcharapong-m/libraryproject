# from django.conf.urls import url 
from django.urls import path
from myapp import views 
from django.contrib import admin

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('entertainment/', views.Fetchbytypeentertainment, name='entertainment'),
    path('learning/', views.Fetchbytypelearning, name='learning'),
    path('disabledandelderly/', views.Fetchbytypedisabledandelderly, name='disabledandelderly'),
    path('scienceadntecnology/', views.Fetchbytypescienceadntecnology, name='scienceadntecnology'),
    path('mobileapplication/', views.Fetchbytypemobileapplication, name='mobileapplication'),
    path('<str:year>/',views.year, name='year'),
    path('<int:id>/detail',views.detail, name='detail'),
    path('all/', views.dataAll, name='dataall'),
    path('search/', views.search, name='search'),
    path('',views.index, name='index'),
]