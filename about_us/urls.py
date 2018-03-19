from django.conf.urls import url

from . import views

app_name = "about_us"
urlpatterns = [
    url(r'^$', views.AboutUsView.as_view(), name='about_us')
]
