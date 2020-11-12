from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('<slug:slug>', DetailedView.as_view(), name="post_detail_view"),
]