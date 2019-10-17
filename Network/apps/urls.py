from django.urls import path, re_path, include
from . network_base.views import PostView


urlpatterns = [
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # POST
    re_path(r'^post/like/(?P<pk>\d+)/$', PostView.as_view({'get': 'list'}), name='post_like'),
    re_path(r'^post/unlike/(?P<pk>\d+)/$', PostView.as_view({'get': 'list'}), name='post_unlike'),
    re_path(r'^post/', PostView.as_view({'post': 'create'}), name='post_create'),
]
