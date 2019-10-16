from django.urls import path, re_path, include

from . network_base import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
