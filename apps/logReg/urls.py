from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^success$', views.success),
    url(r'^log_in$', views.log_in),
    url(r'^log_off$', views.log_off),

]
