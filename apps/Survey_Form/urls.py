from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index ),
    url(r'^index$', views.index ),
    url(r'^process$', views.form_process ),
]