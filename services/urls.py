from django.conf.urls import url

from services import views

urlpatterns = [
    url(r'add/', views.ServiceCreateView.as_view(), name='add'),
    url(r'update/(?P<pk>[0-9]+)/$', views.ServiceUpdateView.as_view(), name='update'),
    url(r'list/', views.ServiceListView.as_view(), name='list'),
    url(r'delete/(?P<pk>[0-9]+)/$', views.ServiceDeleteView.as_view(), name='delete'),
]
