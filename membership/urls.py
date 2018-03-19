from django.conf.urls import url, re_path
from manchug import urls
from . import views
app_name = "membership"
urlpatterns = [
    # url(r'^$', views.membership_view, name='membership'),
    # re_path(r'^$', views.membership_view, name='membership'),
    re_path(r'^$', views.ContactFormView.as_view(), name='membership'),
]
