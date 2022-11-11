from django.urls import path
from .views import MyViews

urlpatterns = [
    path('mv/', MyViews.as_view())
]