from django.urls import path

from . import views
from . import shelf_views

app_name = "tracker"

urlpatterns = [
    path("following/", shelf_views.shelf, name="shelf"),
    path("<int:novel_id>/follow/", shelf_views.follow, name="follow"),
    path("<int:novel_id>/", views.novel_detail, name="novel_detail"),
    path("<int:novel_id>/chapters/<int:chapter_id>/", views.chapter_detail, name="chapter_detail"),
    path("<int:novel_id>/<str:entry_type>/<int:entry_id>/read/", views.mark_read, name="mark_read"),
]
