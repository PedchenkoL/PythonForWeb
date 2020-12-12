from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name = 'home'),
    path('adaptive', views.about, name = 'about-us'),
    path('paint', views.paint, name = 'paint'),
    path('paintAdaptive', views.paintAdaptive, name = 'paintAdaptive'),
    # path('home', views.index),
    path('post_list', views.post_list, name = 'post_list'),
    path('admin', views.post_list, name = 'admin'),

]
