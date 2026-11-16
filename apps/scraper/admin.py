from django.contrib import admin
from .models import Tag, Novel, NovelTag, Chapter, Job


class NovelTagInline(admin.TabularInline):
    model = NovelTag
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "status", "rating", "total_pages", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "author_name", "royalroad_id")
    inlines = [NovelTagInline]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("novel", "chapter_number", "title", "word_count", "scraped_at")
    list_filter = ("novel",)
    search_fields = ("title", "content", "royalroad_chapter_id")


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "target_url", "status", "chapters_scraped", "started_at")
    list_filter = ("status", "started_at")
    search_fields = ("target_url", "user__username")
