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
    path('2563/',views.year2563, name='2563'),
    path('2564/',views.year2564, name='2564'),
    path('2565/',views.year2565, name='2565'),
    path('2566/',views.year2566, name='2566'),
    path('2567/',views.year2567, name='2567'),
    # path('detail/',views.detail, name='detail'),
    path('<int:id>/detail',views.detail, name='detail'),
    path('all/', views.dataAll, name='dataall'),
    path('search/', views.search, name='search'),
    path('',views.index, name='index'),



    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)