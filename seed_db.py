import os
import django
from decimal import Decimal
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User
from apps.profile.models import Profile
from apps.user_settings.models import UserSettings
from apps.scraper.models import Tag, Novel, Chapter, Job, NovelTag
from apps.tracker.models import Bookmark

def seed():
    print("Seeding database with realistic sample data...")

    # 1. Update/Ensure User 'Yoji' has profile and settings filled
    user = User.objects.filter(username="Yoji").first()
    if not user:
        user = User.objects.first()

    if user:
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.full_name = "Yoji Macadangdang"
        profile.bio = "Avid fantasy reader and aspiring software engineer studying CSIT327."
        profile.save()

        settings_obj, _ = UserSettings.objects.get_or_create(user=user)
        settings_obj.dark_mode = True
        settings_obj.email_notifications = True
        settings_obj.save()
        print(f"Updated profile & settings for user: {user.username}")

    # 2. Seed Tags (scraper_tag)
    tags_data = [
        {"name": "Progression", "slug": "progression"},
        {"name": "LitRPG", "slug": "litrpg"},
        {"name": "Fantasy", "slug": "fantasy"},
        {"name": "Time Loop", "slug": "time-loop"},
        {"name": "Adventure", "slug": "adventure"},
        {"name": "Sci-Fi", "slug": "sci-fi"},
    ]
    tag_objs = {}
    for t in tags_data:
        tag, _ = Tag.objects.get_or_create(slug=t["slug"], defaults={"name": t["name"]})
        tag_objs[t["slug"]] = tag
    print(f"Seeded {len(tag_objs)} tags into scraper_tag.")

    # 3. Seed Novels (scraper_novel)
    novels_data = [
        {
            "royalroad_id": "21220",
            "title": "Mother of Learning",
            "author_name": "nobody103",
            "synopsis": "Zorian Kazinski is a teenage mage of humble birth and slightly above average skill, attending his third year of education at Cyoria's magical academy. A sudden invasion plunges the city into chaos, and Zorian finds himself thrown back in time to the beginning of the month.",
            "cover_image_url": "https://www.royalroad.com/covers/21220.jpg",
            "status": "COMPLETED",
            "rating": Decimal("4.88"),
            "total_pages": 2865,
            "source_url": "https://www.royalroad.com/fiction/21220/mother-of-learning",
            "tags": ["fantasy", "time-loop", "progression"],
        },
        {
            "royalroad_id": "26294",
            "title": "The Primal Hunter",
            "author_name": "Zogarth",
            "synopsis": "Jake leads an unremarkable life as an office worker until the entire multiverse is integrated into the System. Thrust into a tutorial wilderness, Jake discovers his true calling as an instinct-driven hunter and alchemist.",
            "cover_image_url": "https://www.royalroad.com/covers/26294.jpg",
            "status": "ONGOING",
            "rating": Decimal("4.62"),
            "total_pages": 4500,
            "source_url": "https://www.royalroad.com/fiction/26294/the-primal-hunter",
            "tags": ["litrpg", "progression", "adventure"],
        },
        {
            "royalroad_id": "24709",
            "title": "Defiance of the Fall",
            "author_name": "TheFirstDefier",
            "synopsis": "Zac was on a camping trip when the world changed, merging Earth with the broader multiverse. Armed with only a lumberjack axe, he must battle otherworldly beasts to survive.",
            "cover_image_url": "https://www.royalroad.com/covers/24709.jpg",
            "status": "ONGOING",
            "rating": Decimal("4.55"),
            "total_pages": 5200,
            "source_url": "https://www.royalroad.com/fiction/24709/defiance-of-the-fall",
            "tags": ["litrpg", "fantasy", "adventure"],
        },
    ]

    novel_objs = {}
    for nd in novels_data:
        novel, created = Novel.objects.get_or_create(
            royalroad_id=nd["royalroad_id"],
            defaults={
                "title": nd["title"],
                "author_name": nd["author_name"],
                "synopsis": nd["synopsis"],
                "cover_image_url": nd["cover_image_url"],
                "status": nd["status"],
                "rating": nd["rating"],
                "total_pages": nd["total_pages"],
                "source_url": nd["source_url"],
            }
        )
        novel_objs[nd["royalroad_id"]] = novel
        # Seed M:N junction (scraper_novel_tags)
        for t_slug in nd["tags"]:
            tag_instance = tag_objs.get(t_slug)
            if tag_instance:
                NovelTag.objects.get_or_create(novel=novel, tag=tag_instance)
    print(f"Seeded {len(novel_objs)} novels into scraper_novel.")

    # 4. Seed Chapters (scraper_chapter)
    mol = novel_objs.get("21220")
    if mol:
        ch_data = [
            {
                "royalroad_chapter_id": "21220-1",
                "chapter_number": 1,
                "title": "Good Morning Brother",
                "content": "Zorian woke up abruptly to the sound of something screeching into his ear. He flailed around blindly for several seconds before realizing it was his alarm clock...",
                "word_count": 4820,
                "source_url": "https://www.royalroad.com/fiction/21220/chapter/1",
            },
            {
                "royalroad_chapter_id": "21220-2",
                "chapter_number": 2,
                "title": "The Academy of Cyoria",
                "content": "The train journey to Cyoria was long and uneventful, exactly as Zorian preferred it. Taking out his notebook, he reviewed his preparatory magical algebra theorems...",
                "word_count": 5120,
                "source_url": "https://www.royalroad.com/fiction/21220/chapter/2",
            },
            {
                "royalroad_chapter_id": "21220-3",
                "chapter_number": 3,
                "title": "The Month of the Cataclysm",
                "content": "A deafening blast shattered the tranquil evening. Looking out the academy tower window, red beams sliced through the sky as the Sovereign Gate hummed with unnatural resonance...",
                "word_count": 6430,
                "source_url": "https://www.royalroad.com/fiction/21220/chapter/3",
            },
        ]
        for c in ch_data:
            Chapter.objects.get_or_create(
                novel=mol,
                royalroad_chapter_id=c["royalroad_chapter_id"],
                defaults={
                    "chapter_number": c["chapter_number"],
                    "title": c["title"],
                    "content": c["content"],
                    "word_count": c["word_count"],
                    "source_url": c["source_url"],
                    "release_date": timezone.now(),
                }
            )
        print("Seeded chapters into scraper_chapter.")

    # 5. Seed Scraper Jobs (scraper_job)
    if user and mol:
        jobs_data = [
            {
                "novel": mol,
                "target_url": mol.source_url,
                "status": "COMPLETED",
                "chapters_scraped": 3,
                "error_message": None,
                "completed_at": timezone.now(),
            },
            {
                "novel": novel_objs.get("26294"),
                "target_url": "https://www.royalroad.com/fiction/26294/the-primal-hunter",
                "status": "PENDING",
                "chapters_scraped": 0,
                "error_message": None,
                "completed_at": None,
            },
        ]
        for j in jobs_data:
            Job.objects.get_or_create(
                user=user,
                target_url=j["target_url"],
                defaults={
                    "novel": j["novel"],
                    "status": j["status"],
                    "chapters_scraped": j["chapters_scraped"],
                    "error_message": j["error_message"],
                    "completed_at": j["completed_at"],
                }
            )
        print("Seeded jobs into scraper_job.")

    # 6. Seed Bookmarks (tracker_bookmark)
    if user and mol:
        last_ch = Chapter.objects.filter(novel=mol, chapter_number=2).first()
        Bookmark.objects.get_or_create(
            user=user,
            novel=mol,
            defaults={
                "last_read_chapter": last_ch,
                "reading_status": "READING",
                "is_favorite": True,
            }
        )
        primal = novel_objs.get("26294")
        if primal:
            Bookmark.objects.get_or_create(
                user=user,
                novel=primal,
                defaults={
                    "last_read_chapter": None,
                    "reading_status": "PLAN_TO_READ",
                    "is_favorite": False,
                }
            )
        print("Seeded bookmarks into tracker_bookmark.")

    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed()
