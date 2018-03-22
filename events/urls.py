from django.conf.urls import url
from django.urls import re_path

from . import views

app_name = "events"
urlpatterns = [
    url(r'^$', views.EventsView.as_view(), name='events'),
    # url(r'^event_detail/$', views.event_detail_view, name='event_detail'),
    re_path(r'^event_one/$', views.EventOneView.as_view(), name='event_one'),
    re_path(r'^event_two/$', views.EventTwoView.as_view(), name='event_two'),
]
