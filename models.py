"""
Entities Represented:
1. auth_user                  (Django Core Authentication)
2. profile_profile            (Profile Slice: Profile)
3. user_settings_usersettings (Settings Slice: UserSettings)
4. scraper_tag                (Scraper Slice: Tag)
5. scraper_novel              (Scraper Slice: Novel)
6. scraper_novel_tags         (Scraper Slice: NovelTag Junction Table M:N)
7. scraper_chapter            (Scraper Slice: Chapter)
8. scraper_job                (Scraper Slice: Job)
9. tracker_bookmark           (Tracker Slice: Bookmark)
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# ==============================================================================
# 1. USER PROFILE VERTICAL SLICE (apps.profile)
# ==============================================================================

class Profile(models.Model):
    """
    Corresponds to 'profile_profile' table in the approved ERD.
    Cardinality: auth_user (1) <-> (1) profile_profile
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    full_name = models.CharField(max_length=150, blank=True, default="")
    bio = models.TextField(blank=True, default="")
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    class Meta:
        db_table = "profile_profile"
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"Profile of {self.user.username}"


# ==============================================================================
# 2. USER SETTINGS VERTICAL SLICE (apps.user_settings)
# ==============================================================================

class UserSettings(models.Model):
    """
    Corresponds to 'user_settings_usersettings' table in the approved ERD.
    Cardinality: auth_user (1) <-> (1) user_settings_usersettings
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="settings"
    )
    dark_mode = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)

    class Meta:
        db_table = "user_settings_usersettings"
        verbose_name = "User Settings"
        verbose_name_plural = "User Settings"

    def __str__(self):
        return f"Settings for {self.user.username}"


# ==============================================================================
# 3. SCRAPER & FICTION CORE VERTICAL SLICE (apps.scraper)
# ==============================================================================

class Tag(models.Model):
    """
    Corresponds to 'scraper_tag' table in the approved ERD.
    Stores novel thematic genres and tags.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        db_table = "scraper_tag"
        verbose_name = "Fiction Tag"
        verbose_name_plural = "Fiction Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Novel(models.Model):
    """
    Corresponds to 'scraper_novel' table in the approved ERD.
    Stores core Royal Road fiction metadata.
    """
    STATUS_CHOICES = [
        ("ONGOING", "Ongoing"),
        ("COMPLETED", "Completed"),
        ("HIATUS", "Hiatus"),
        ("STUB", "Stub"),
    ]

    royalroad_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=150)
    synopsis = models.TextField(blank=True, null=True)
    cover_image_url = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=30, default="ONGOING", choices=STATUS_CHOICES)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    total_pages = models.IntegerField(default=0)
    source_url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(
        Tag,
        through="NovelTag",
        related_name="novels",
        blank=True
    )

    class Meta:
        db_table = "scraper_novel"
        verbose_name = "Novel"
        verbose_name_plural = "Novels"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


class NovelTag(models.Model):
    """
    Corresponds to 'scraper_novel_tags' junction table in the approved ERD.
    Cardinality: scraper_novel (M) <-> (N) scraper_tag
    """
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = "scraper_novel_tags"
        unique_together = ("novel", "tag")
        verbose_name = "Novel Tag Mapping"
        verbose_name_plural = "Novel Tag Mappings"

    def __str__(self):
        return f"{self.novel.title} <-> {self.tag.name}"


class Chapter(models.Model):
    """
    Corresponds to 'scraper_chapter' table in the approved ERD.
    Cardinality: scraper_novel (1) <-> (N) scraper_chapter
    """
    novel = models.ForeignKey(
        Novel,
        on_delete=models.CASCADE,
        related_name="chapters"
    )
    royalroad_chapter_id = models.CharField(max_length=50)
    chapter_number = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    word_count = models.IntegerField(default=0)
    source_url = models.CharField(max_length=500)
    release_date = models.DateTimeField(null=True, blank=True)
    scraped_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "scraper_chapter"
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"
        ordering = ["novel", "chapter_number"]

    def __str__(self):
        return f"{self.novel.title} - Ch. {self.chapter_number}: {self.title}"


class Job(models.Model):
    """
    Corresponds to 'scraper_job' table in the approved ERD.
    Cardinality: auth_user (1) <-> (N) scraper_job
                 scraper_novel (1) <-> (0..N) scraper_job
    """
    JOB_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("RUNNING", "Running"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="scraper_jobs"
    )
    novel = models.ForeignKey(
        Novel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="scraper_jobs"
    )
    target_url = models.CharField(max_length=500)
    status = models.CharField(max_length=30, default="PENDING", choices=JOB_STATUS_CHOICES)
    chapters_scraped = models.IntegerField(default=0)
    error_message = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "scraper_job"
        verbose_name = "Scraper Job"
        verbose_name_plural = "Scraper Jobs"
        ordering = ["-started_at"]

    def __str__(self):
        return f"Job #{self.id} [{self.status}] - {self.target_url}"


# ==============================================================================
# 4. USER READING TRACKER & BOOKMARK SLICE (apps.tracker)
# ==============================================================================

class Bookmark(models.Model):
    """
    Corresponds to 'tracker_bookmark' table in the approved ERD.
    Cardinality: auth_user (1) <-> (N) tracker_bookmark
                 scraper_novel (1) <-> (N) tracker_bookmark
                 scraper_chapter (0..1) <-> (N) tracker_bookmark
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
        Novel,
        on_delete=models.CASCADE,
        related_name="bookmarks"
    )
    last_read_chapter = models.ForeignKey(
        Chapter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookmarks"
    )
    reading_status = models.CharField(
        max_length=30,
        default="READING",
        choices=READING_STATUS_CHOICES
    )
    is_favorite = models.BooleanField(default=False)
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
