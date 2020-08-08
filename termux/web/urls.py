from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/?$', views.register, name='register'),
    url(r'^getToken/?$', views.getToken, name='getToken'),
    url(r'^s/call_log/?$', views.s_call_log, name='s_call_log'),
    url(r'^s/sms_list/?$', views.s_sms_list, name='s_sms_list'),
    url(r'^s/contact/?$', views.s_contact, name='s_contact'),
    url(r'^s/clipboard/?$', views.s_clipboard, name='s_clipboard'),
]