from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.index, name='index' ),
    path('scann', views.scann, name='scann'),
    url(r'^qr2/(?<place>\w+)&(?<branch>\w+)&(?<server>\w+)/$',views.qr2)



]
