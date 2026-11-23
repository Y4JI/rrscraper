from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Bookmark(models.Model):
    """
    Corresponds to 'tracker_bookmark' entity in the approved ERD.
    Tracks user reading list, bookmarks, progress, and favorites.
    """
    READING_STATUS_CHOICES = [
        ("READING", "Reading"),
        ("PLAN_TO_READ", "Plan to Read"),
        ("COMPLETED", "Completed"),
        ("DROPPED", "Dropped"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookmarks"
    )
    novel = models.ForeignKey(
        "scraper.Novel",
        on_delete=models.CASCADE,
        related_name="bookmarks"
    )
    last_read_chapter = models.ForeignKey(
        "scraper.Chapter",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookmarks"
    )
    last_read_release = models.ForeignKey(
        "scraper.ChapterRelease",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookmarks",
    )
    reading_status = models.CharField(
        max_length=30,
        default="READING",
        choices=READING_STATUS_CHOICES
    )
    is_favorite = models.BooleanField(default=False)
    is_following = models.BooleanField(default=True)
    last_read_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tracker_bookmark"
        unique_together = ("user", "novel")
        verbose_name = "User Bookmark"
        verbose_name_plural = "User Bookmarks"
        ordering = ["-last_read_at"]

    def __str__(self):
        return f"{self.user.username} - {self.novel.title} [{self.reading_status}]"
