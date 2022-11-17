from django.urls import path
from .views import myView

urlpatterns = [
    path("project/", myView, name="pform")
]