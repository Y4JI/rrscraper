-- ====================================================================
-- PHYSICAL DATABASE SCHEMA (PostgreSQL 17 / Supabase)
-- Proposed System: Royal Road Scraper (rrscraper)
-- Course: CSIT327 | Student: Yoji Macadangdang
-- ====================================================================
-- TIP FOR DRAW.IO:
-- In draw.io, go to: Arrange -> Insert -> Advanced -> SQL
-- Paste this entire file to instantly generate native ERD diagram blocks!
-- ====================================================================

-- 1. Core Authentication Table (Django Managed)
CREATE TABLE auth_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    email VARCHAR(254) NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,
    is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
    date_joined TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMPTZ
);

-- 2. User Profile Vertical Slice (apps/profile/models.py)
CREATE TABLE profile_profile (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE REFERENCES auth_user(id) ON DELETE CASCADE,
    full_name VARCHAR(150) DEFAULT '',
    bio TEXT DEFAULT '',
    profile_image VARCHAR(100)
);

-- 3. User Settings Vertical Slice (apps/user_settings/models.py)
CREATE TABLE user_settings_usersettings (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE REFERENCES auth_user(id) ON DELETE CASCADE,
    dark_mode BOOLEAN NOT NULL DEFAULT FALSE,
    email_notifications BOOLEAN NOT NULL DEFAULT TRUE
);

-- 4. Royal Road Fiction / Novel Entity
CREATE TABLE scraper_novel (
    id BIGSERIAL PRIMARY KEY,
    royalroad_id VARCHAR(50) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    author_name VARCHAR(150) NOT NULL,
    synopsis TEXT,
    cover_image_url VARCHAR(500),
    status VARCHAR(30) NOT NULL DEFAULT 'ONGOING',
    rating NUMERIC(3, 2),
    total_pages INTEGER NOT NULL DEFAULT 0,
    source_url VARCHAR(500) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 5. Novel Chapters Scraped & Downloaded
CREATE TABLE scraper_chapter (
    id BIGSERIAL PRIMARY KEY,
    novel_id BIGINT NOT NULL REFERENCES scraper_novel(id) ON DELETE CASCADE,
    royalroad_chapter_id VARCHAR(50) NOT NULL,
    chapter_number INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    word_count INTEGER NOT NULL DEFAULT 0,
    source_url VARCHAR(500) NOT NULL,
    release_date TIMESTAMPTZ,
    scraped_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 6. Fiction Tags & Genres
CREATE TABLE scraper_tag (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    slug VARCHAR(50) NOT NULL UNIQUE
);

-- 7. Novel <-> Tags Junction Table (Many-to-Many)
CREATE TABLE scraper_novel_tags (
    id BIGSERIAL PRIMARY KEY,
    novel_id BIGINT NOT NULL REFERENCES scraper_novel(id) ON DELETE CASCADE,
    tag_id BIGINT NOT NULL REFERENCES scraper_tag(id) ON DELETE CASCADE,
    CONSTRAINT uq_novel_tag UNIQUE (novel_id, tag_id)
);

-- 8. Scraper Execution Tasks & Status Tracker
CREATE TABLE scraper_job (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES auth_user(id) ON DELETE CASCADE,
    novel_id BIGINT REFERENCES scraper_novel(id) ON DELETE SET NULL,
    target_url VARCHAR(500) NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'PENDING',
    chapters_scraped INTEGER NOT NULL DEFAULT 0,
    error_message TEXT,
    started_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMPTZ
);

-- 9. User Reading Library & Bookmark Tracker
CREATE TABLE tracker_bookmark (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES auth_user(id) ON DELETE CASCADE,
    novel_id BIGINT NOT NULL REFERENCES scraper_novel(id) ON DELETE CASCADE,
    last_read_chapter_id BIGINT REFERENCES scraper_chapter(id) ON DELETE SET NULL,
    reading_status VARCHAR(30) NOT NULL DEFAULT 'READING',
    is_favorite BOOLEAN NOT NULL DEFAULT FALSE,
    last_read_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_user_novel_bookmark UNIQUE (user_id, novel_id)
);
