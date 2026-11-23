from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    Corresponds to 'scraper_tag' entity in the approved ERD.
    Stores novel tags and genres.
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
    Corresponds to 'scraper_novel' entity in the approved ERD.
    Stores web fiction metadata scraped from Royal Road.
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
    tags = models.ManyToManyField(Tag, through="NovelTag", related_name="novels", blank=True)

    class Meta:
        db_table = "scraper_novel"
        verbose_name = "Novel"
        verbose_name_plural = "Novels"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


class NovelTag(models.Model):
    """
    Corresponds to 'scraper_novel_tags' junction entity in the approved ERD.
    Establishes Many-to-Many relationship between Novel and Tag.
    """
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = "scraper_novel_tags"
        unique_together = ("novel", "tag")
        verbose_name = "Novel Tag Mapping"
        verbose_name_plural = "Novel Tag Mappings"

    def __str__(self):
        return f"{self.novel.title} - {self.tag.name}"


class Chapter(models.Model):
    """
    Corresponds to 'scraper_chapter' entity in the approved ERD.
    Stores downloaded novel chapters and text content.
    """
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name="chapters")
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
        constraints = [
            models.UniqueConstraint(
                fields=["novel", "royalroad_chapter_id"], name="unique_novel_source_chapter"
            )
        ]

    def __str__(self):
        return f"{self.novel.title} - Ch. {self.chapter_number}: {self.title}"


class ChapterRelease(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name="releases")
    royalroad_chapter_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    source_url = models.URLField(max_length=500)
    release_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = [models.F("release_date").desc(nulls_last=True), "-pk"]
        constraints = [
            models.UniqueConstraint(
                fields=["novel", "royalroad_chapter_id"], name="unique_novel_release"
            )
        ]

    def __str__(self):
        return self.title


class Job(models.Model):
    """
    Corresponds to 'scraper_job' entity in the approved ERD.
    Tracks scraping execution runs, progress, and error logs.
    """
    JOB_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("RUNNING", "Running"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]

    class Source(models.TextChoices):
        LEGACY = "LEGACY", "Earlier import"
        RSS = "RSS", "Royal Road RSS"
        WEB = "WEB", "Royal Road website"
        AUTHOR = "AUTHOR", "Author-provided export"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scraper_jobs")
    novel = models.ForeignKey(
        Novel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="scraper_jobs"
    )
    target_url = models.CharField(max_length=500)
    source = models.CharField(max_length=10, choices=Source.choices, default=Source.LEGACY)
    status = models.CharField(max_length=30, default="PENDING", choices=JOB_STATUS_CHOICES)
    chapters_scraped = models.IntegerField(default=0)
    releases_imported = models.PositiveIntegerField(default=0)
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
