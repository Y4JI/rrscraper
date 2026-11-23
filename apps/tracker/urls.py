from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("<int:novel_id>/", views.novel_detail, name="novel_detail"),
    path("<int:novel_id>/chapters/<int:chapter_id>/", views.chapter_detail, name="chapter_detail"),
    path("<int:novel_id>/<str:entry_type>/<int:entry_id>/read/", views.mark_read, name="mark_read"),
]
