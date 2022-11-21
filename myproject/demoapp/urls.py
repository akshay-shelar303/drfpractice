from django.urls import path
from .views import myView, showView

urlpatterns = [
    path("project/", myView, name="pform"),
    path("show/", showView, name="show"),
]