from django.contrib import admin
from .models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "novel", "reading_status", "is_favorite", "last_read_at")
    list_filter = ("reading_status", "is_favorite")
    search_fields = ("user__username", "novel__title")
