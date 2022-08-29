from __future__ import unicode_literals
try:
    from django.urls import re_path,path
except ImportError:
    # For Django 1.8 compatibility
    from django.conf.urls import url as re_path

from forms import views


urlpatterns = [
    re_path(r"(?P<slug>.*)/sent/$", views.form_sent, name="form_sent"),
    re_path(r"(?P<slug>.*)/$", views.FormDetail.as_view(), name="form_detail"),
    # re_path(r"(?P<slug>.*)/data/$", views.FormData, name="formdata"),
]
