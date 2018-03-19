from django.conf.urls import url

from . import views
app_name = "committee"
urlpatterns = [
    url(r'^$', views.CommitteeView.as_view(), name='committee')
]
