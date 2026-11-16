# Physical Entity-Relationship Diagram (ERD) Documentation

**Course:** CSIT327  
**Proposed System:** Royal Road Scraper & Web Fiction Tracker (`rrscraper`)  
**Student:** Yoji Macadangdang  
**Submission Filename:** `MACADANGDANG_ERD.pdf`  
**Database Engine:** PostgreSQL 17 (Hosted on Supabase)  
**Framework & Architecture:** Django 5.2 (Vertical Slice Architecture)

---

## 1. Executive Summary

The proposed system, **Royal Road Scraper (`rrscraper`)**, is a web fiction discovery, scraping, and chapter tracking application. Built with Django and backed by a hosted Supabase PostgreSQL database, it allows authenticated users to search fiction, trigger scraper jobs to retrieve novels and chapters from Royal Road, track reading progress, bookmark favorites, and manage user profile and application preferences.

The **Physical Entity-Relationship Diagram (ERD)** defines the concrete database schema, including:
- Concrete PostgreSQL data types (`INTEGER`, `BIGINT`, `VARCHAR`, `TEXT`, `BOOLEAN`, `NUMERIC`, `TIMESTAMPTZ`).
- Primary Keys (`PK`) and Foreign Keys (`FK`) with cascade and nullify referential integrity actions.
- Explicit Unique (`UQ`) and Default (`DF`) constraints.
- Cardinality rules expressed in **Crow's Foot notation**.

---

## 2. Included Project Deliverables

| File | Description | Usage / Target |
|---|---|---|
| **[`MACADANGDANG_ERD.pdf`](file:///c:/Users/MyPC/3RDYR-CS/rrscraper/MACADANGDANG_ERD.pdf)** | Ready-to-submit official physical ERD in vector PDF format. | Direct classroom assignment submission. |
| **[`MACADANGDANG_ERD.drawio`](file:///c:/Users/MyPC/3RDYR-CS/rrscraper/MACADANGDANG_ERD.drawio)** | Native draw.io / diagrams.net XML diagram file. | Open directly in draw.io to view, rearrange, style, or edit. |
| **[`schema_erd.sql`](file:///c:/Users/MyPC/3RDYR-CS/rrscraper/schema_erd.sql)** | Complete PostgreSQL DDL (`CREATE TABLE` with PKs, FKs, constraints). | Import via draw.io (`Arrange > Insert > Advanced > SQL`). |
| **[`erd_mermaid.mmd`](file:///c:/Users/MyPC/3RDYR-CS/rrscraper/erd_mermaid.mmd)** | Mermaid ER Diagram script. | Import via draw.io (`Arrange > Insert > Advanced > Mermaid`). |
| **[`MACADANGDANG_ERD.html`](file:///c:/Users/MyPC/3RDYR-CS/rrscraper/MACADANGDANG_ERD.html)** | Standalone interactive HTML render with SVG Crow's Foot overlay. | Browser viewing and printing. |

---

## 3. How to Use in draw.io (3 Options)

### Option A: Open Native `.drawio` File Directly (Recommended)
1. Go to **[draw.io](https://app.diagrams.net/)** (or use the VS Code Draw.io extension).
2. Click **File** &rarr; **Open From** &rarr; **Device...** (or drag and drop).
3. Select `MACADANGDANG_ERD.drawio` from your project folder:
   `c:\Users\MyPC\3RDYR-CS\rrscraper\MACADANGDANG_ERD.drawio`
4. All tables, columns, PK/FK styling, and Crow's foot connectors will render cleanly as native editable vector shapes.
5. To export: Click **File** &rarr; **Export as** &rarr; **PDF** &rarr; Save as `MACADANGDANG_ERD.pdf`.

### Option B: Import via SQL DDL
1. Open **[draw.io](https://app.diagrams.net/)**.
2. Click **Arrange** &rarr; **Insert** &rarr; **Advanced** &rarr; **SQL**.
3. Open [`schema_erd.sql`](file:///c:/Users/MyPC/3RDYR-CS/rrscraper/schema_erd.sql), copy all text, and paste into the prompt.
4. Click **Insert**. Draw.io will automatically construct all 9 entity tables with all attributes, data types, and primary keys.

### Option C: Import via Mermaid
1. Open **[draw.io](https://app.diagrams.net/)**.
2. Click **Arrange** &rarr; **Insert** &rarr; **Advanced** &rarr; **Mermaid**.
3. Open [`erd_mermaid.mmd`](file:///c:/Users/MyPC/3RDYR-CS/rrscraper/erd_mermaid.mmd), copy all text, and paste into the prompt.
4. Click **Insert**. Draw.io will generate the ER diagram and connect relationships automatically.

---

## 4. Physical Data Dictionary

### 4.1. Identity & Vertical Slice Module

#### 1. `auth_user` (Django Core Authentication)
*Source: Supabase PostgreSQL / Django Auth*
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `INTEGER` | **PK**, NOT NULL | Auto-incrementing primary key |
| `username` | `VARCHAR(150)` | **UQ**, NOT NULL | Unique login handle |
| `password` | `VARCHAR(128)` | NOT NULL | PBKDF2 / Argon2 hashed password |
| `email` | `VARCHAR(254)` | NOT NULL | User contact email |
| `first_name` | `VARCHAR(150)` | NOT NULL | First name |
| `last_name` | `VARCHAR(150)` | NOT NULL | Last name / surname |
| `is_active` | `BOOLEAN` | NOT NULL, DEFAULT `true` | Account active flag |
| `is_staff` | `BOOLEAN` | NOT NULL, DEFAULT `false` | Access to admin panel |
| `is_superuser`| `BOOLEAN` | NOT NULL, DEFAULT `false` | Superuser permissions |
| `date_joined` | `TIMESTAMPTZ` | NOT NULL | Timestamp when registered |
| `last_login` | `TIMESTAMPTZ` | NULLABLE | Timestamp of last authentication |

#### 2. `profile_profile` (User Profile Slice)
*Source: `apps/profile/models.py`*
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `BIGINT` | **PK**, NOT NULL | Auto-incrementing primary key |
| `user_id` | `INTEGER` | **FK**, **UQ**, NOT NULL | `REFERENCES auth_user(id) ON DELETE CASCADE` (1:1) |
| `full_name` | `VARCHAR(150)` | NULLABLE | Display name |
| `bio` | `TEXT` | NULLABLE | User biography / description |
| `profile_image` | `VARCHAR(100)` | NULLABLE | Avatar media path in Supabase / storage |

#### 3. `user_settings_usersettings` (Settings Slice)
*Source: `apps/user_settings/models.py`*
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `BIGINT` | **PK**, NOT NULL | Auto-incrementing primary key |
| `user_id` | `INTEGER` | **FK**, **UQ**, NOT NULL | `REFERENCES auth_user(id) ON DELETE CASCADE` (1:1) |
| `dark_mode` | `BOOLEAN` | NOT NULL, DEFAULT `false` | UI dark theme preference |
| `email_notifications` | `BOOLEAN` | NOT NULL, DEFAULT `true` | Email alert toggle |

---

### 4.2. Core Scraper & Fiction Module

#### 4. `scraper_novel` (Royal Road Fiction Record)
*Source: Core domain entity reflected in `templates/home/home.html`*
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `BIGINT` | **PK**, NOT NULL | Auto-incrementing primary key |
| `royalroad_id` | `VARCHAR(50)` | **UQ**, NOT NULL | Unique fiction ID on Royal Road |
| `title` | `VARCHAR(255)` | NOT NULL | Fiction title |
| `author_name` | `VARCHAR(150)` | NOT NULL | Fiction author |
| `synopsis` | `TEXT` | NULLABLE | Novel summary / blurb |
| `cover_image_url` | `VARCHAR(500)` | NULLABLE | Remote cover art URL |
| `status` | `VARCHAR(30)` | NOT NULL, DEFAULT `'ONGOING'` | Status (`ONGOING`, `COMPLETED`, `HIATUS`) |
| `rating` | `NUMERIC(3, 2)`| NULLABLE | Average rating (0.00 – 5.00) |
| `total_pages` | `INTEGER` | NOT NULL, DEFAULT `0` | Estimated page count |
| `source_url` | `VARCHAR(500)` | NOT NULL | Full URL to the fiction on Royal Road |
| `created_at` | `TIMESTAMPTZ` | NOT NULL | Timestamp when novel was first scraped |
| `updated_at` | `TIMESTAMPTZ` | NOT NULL | Timestamp of last metadata update |

#### 5. `scraper_chapter` (Fiction Chapters Downloaded)
*Source: Chapters downloaded count in home dashboard*
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `BIGINT` | **PK**, NOT NULL | Auto-incrementing primary key |
| `novel_id` | `BIGINT` | **FK**, NOT NULL | `REFERENCES scraper_novel(id) ON DELETE CASCADE` (1:N) |
| `royalroad_chapter_id` | `VARCHAR(50)` | NOT NULL | Chapter ID on Royal Road |
| `chapter_number` | `INTEGER` | NOT NULL | Sequential chapter index |
| `title` | `VARCHAR(255)` | NOT NULL | Chapter heading |
| `content` | `TEXT` | NOT NULL | Scraped chapter HTML or text body |
| `word_count` | `INTEGER` | NOT NULL, DEFAULT `0` | Calculated word count |
| `source_url` | `VARCHAR(500)` | NOT NULL | Source link on Royal Road |
| `release_date`| `TIMESTAMPTZ` | NULLABLE | Published date on Royal Road |
| `scraped_at` | `TIMESTAMPTZ` | NOT NULL | Timestamp when scraped into database |

#### 6. `scraper_tag` (Genres & Tags)
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `BIGINT` | **PK**, NOT NULL | Auto-incrementing primary key |
| `name` | `VARCHAR(50)` | **UQ**, NOT NULL | Tag name (e.g., *LitRPG*, *Progression*, *Fantasy*) |
| `slug` | `VARCHAR(50)` | **UQ**, NOT NULL | URL-friendly slug |

#### 7. `scraper_novel_tags` (M:N Junction Table)
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `BIGINT` | **PK**, NOT NULL | Auto-incrementing primary key |
| `novel_id` | `BIGINT` | **FK**, NOT NULL | `REFERENCES scraper_novel(id) ON DELETE CASCADE` |
| `tag_id` | `BIGINT` | **FK**, NOT NULL | `REFERENCES scraper_tag(id) ON DELETE CASCADE` |
| — | — | **UQ(`novel_id`, `tag_id`)** | Composite unique constraint |

---

### 4.3. Execution Tasks & User Tracking Module

#### 8. `scraper_job` (Scraper Execution Task & Logs)
*Source: Scraper status indicator in dashboard*
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `BIGINT` | **PK**, NOT NULL | Auto-incrementing primary key |
| `user_id` | `INTEGER` | **FK**, NOT NULL | `REFERENCES auth_user(id) ON DELETE CASCADE` (1:N) |
| `novel_id` | `BIGINT` | **FK**, NULLABLE | `REFERENCES scraper_novel(id) ON DELETE SET NULL` |
| `target_url` | `VARCHAR(500)` | NOT NULL | URL requested to be scraped |
| `status` | `VARCHAR(30)` | NOT NULL, DEFAULT `'PENDING'`| `'PENDING'`, `'RUNNING'`, `'COMPLETED'`, `'FAILED'` |
| `chapters_scraped`| `INTEGER` | NOT NULL, DEFAULT `0` | Number of chapters successfully captured |
| `error_message` | `TEXT` | NULLABLE | Detailed traceback if scraping failed |
| `started_at` | `TIMESTAMPTZ` | NOT NULL | Job initiation timestamp |
| `completed_at` | `TIMESTAMPTZ` | NULLABLE | Job completion timestamp |

#### 9. `tracker_bookmark` (Reading Library & Bookmark Tracker)
*Source: User library and tracking*
| Column Name | Physical Data Type | Key / Constraint | Description |
|---|---|---|---|
| `id` | `BIGINT` | **PK**, NOT NULL | Auto-incrementing primary key |
| `user_id` | `INTEGER` | **FK**, NOT NULL | `REFERENCES auth_user(id) ON DELETE CASCADE` |
| `novel_id` | `BIGINT` | **FK**, NOT NULL | `REFERENCES scraper_novel(id) ON DELETE CASCADE` |
| `last_read_chapter_id` | `BIGINT` | **FK**, NULLABLE | `REFERENCES scraper_chapter(id) ON DELETE SET NULL` |
| `reading_status` | `VARCHAR(30)` | NOT NULL, DEFAULT `'READING'` | `'READING'`, `'PLAN_TO_READ'`, `'COMPLETED'`, `'DROPPED'` |
| `is_favorite`| `BOOLEAN` | NOT NULL, DEFAULT `false` | Favorite novel flag |
| `last_read_at` | `TIMESTAMPTZ` | NOT NULL | Timestamp of last read activity |
| `created_at` | `TIMESTAMPTZ` | NOT NULL | Timestamp when bookmarked |
| — | — | **UQ(`user_id`, `novel_id`)** | Prevents duplicate bookmarks per user |

---

## 5. Relationships & Cardinalities Summary

| # | Parent Table | Child Table | Relationship Type | Cardinality (Crow's Foot) | Foreign Key Field | Referential Integrity |
|---|---|---|---|---|---|---|
| **1** | `auth_user` | `profile_profile` | One-to-One | `1 : 1` (`—\|\|—` to `—\|\|—`) | `profile_profile.user_id` | `ON DELETE CASCADE` |
| **2** | `auth_user` | `user_settings` | One-to-One | `1 : 1` (`—\|\|—` to `—\|\|—`) | `user_settings.user_id` | `ON DELETE CASCADE` |
| **3** | `auth_user` | `scraper_job` | One-to-Many | `1 : N` (`—\|\|—` to `—<`) | `scraper_job.user_id` | `ON DELETE CASCADE` |
| **4** | `auth_user` | `tracker_bookmark`| One-to-Many | `1 : N` (`—\|\|—` to `—<`) | `tracker_bookmark.user_id` | `ON DELETE CASCADE` |
| **5** | `scraper_novel`| `scraper_job` | One-to-Many (Optional) | `1 : 0..N` (`—\|\|—` to `—o<`) | `scraper_job.novel_id` | `ON DELETE SET NULL` |
| **6** | `scraper_novel`| `tracker_bookmark`| One-to-Many | `1 : N` (`—\|\|—` to `—<`) | `tracker_bookmark.novel_id`| `ON DELETE CASCADE` |
| **7** | `scraper_novel`| `scraper_chapter` | One-to-Many | `1 : N` (`—\|\|—` to `—<`) | `scraper_chapter.novel_id` | `ON DELETE CASCADE` |
| **8** | `scraper_novel`| `scraper_novel_tags` | One-to-Many | `1 : N` (`—\|\|—` to `—<`) | `scraper_novel_tags.novel_id` | `ON DELETE CASCADE` |
| **9** | `scraper_tag` | `scraper_novel_tags` | One-to-Many | `1 : N` (`—\|\|—` to `—<`) | `scraper_novel_tags.tag_id` | `ON DELETE CASCADE` |
| **10**| `scraper_chapter`| `tracker_bookmark`| One-to-Many (Optional) | `0..1 : N` (`—o\|—` to `—<`)| `tracker_bookmark.last_read_chapter_id` | `ON DELETE SET NULL` |
