from django.urls import path
from .views import home_view, import_status

app_name = "home"

urlpatterns = [
    path("", home_view, name="home"),
    path("home/", home_view, name="home_alt"),
    path("home/import-status/", import_status, name="import_status"),
]
