from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^$', views.add, name='add'),
        url(r'^home/', views.home, name='home'),
        url(r'^location/', views.location, name="location"),
        url(r'^cabin/', views.cabin, name='cabin'),
        url(r'^landscape/', views.landscape, name='landscape'),
        url(r'^guestbook/', views.guestbook, name='guestbook'),
        url(r'^gmaps/', views.gmaps, name="gmaps"),
        url(r'^index/', views.index, name="index")
]
