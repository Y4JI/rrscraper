# Step 3: Add Profile and Settings Features Summary

## Overview
In accordance with Section 15 of the **CSIT327 Python Django Vertical Slicing and Supabase Guide**, two new vertical slices were implemented: `apps/profile` and `apps/user_settings`. Each feature owns its models, views, forms, URLs, templates, and static assets without cross-feature leakage.

---

## Key Changes Made

### 1. Created Vertical Slices
- **`apps/profile/`**:
  - `models.py`: Defined `Profile` model with `user = OneToOneField(User, on_delete=models.CASCADE)`, `full_name` (CharField), `bio` (TextField), and `profile_image` (`ImageField(upload_to="profile/", blank=True, null=True)`).
  - `forms.py`: `ProfileForm` for editing full name, bio, and uploading profile picture.
  - `views.py`: `profile_view(request)` with login protection, profile retrieval/auto-creation, and form handling.
  - `urls.py`: Configured `app_name = "profile"`, routing `""` to `profile_view`.
  - `admin.py`: Registered `Profile` model in Django Admin with `list_display` and search capability.
  - `tests.py`: Added automated test suite for profile creation, view protection, and updates.
- **`apps/user_settings/`**:
  - `models.py`: Defined `UserSettings` model with `user = OneToOneField(User, on_delete=models.CASCADE)`, `dark_mode` (BooleanField), and `email_notifications` (BooleanField).
  - `forms.py`: `UserSettingsForm` for toggling dark mode and email notifications.
  - `views.py`: `settings_view(request)` with login protection, settings retrieval/auto-creation, and form handling.
  - `urls.py`: Configured `app_name = "user_settings"`, routing `""` to `settings_view`.
  - `admin.py`: Registered `UserSettings` model in Django Admin with `list_display` and filters.
  - `tests.py`: Added automated test suite for settings creation, view protection, and updates.

### 2. Project Configuration (`config/`)
- **`config/settings.py`**:
  - Registered `'apps.profile'` and `'apps.user_settings'` inside `INSTALLED_APPS`.
  - Configured `MEDIA_URL = 'media/'` and `MEDIA_ROOT = BASE_DIR / 'media'` to support image file uploads.
- **`config/urls.py`**:
  - Included `path("profile/", include("apps.profile.urls"))`.
  - Included `path("settings/", include("apps.user_settings.urls"))`.
  - Configured static media route serving in development (`DEBUG = True`).

### 3. Feature-Specific Templates & Static Assets
- **Templates**:
  - `templates/profile/profile.html`: Dedicated profile view and edit interface matching the dark theme, displaying avatar preview, user metadata, and edit form.
  - `templates/user_settings/user_settings.html`: Dedicated settings interface with styled toggle switches for preferences and account details.
  - `templates/home/home.html`: Updated navigation bar with links to Home, Profile, Settings, and Logout.
- **Static Assets**:
  - `static/css/profile/profile.css` & `static/js/profile/profile.js`: Profile styling and live image preview.
  - `static/css/user_settings/user_settings.css` & `static/js/user_settings/user_settings.js`: User settings styling and toggle interactions.
  - `static/images/profile/` & `static/images/user_settings/`: Canonical asset folders.
  - `static/css/home/home.css`: Added `.nav-link` styles.

### 4. Supabase Migrations
- Executed `makemigrations` generating:
  - `apps/profile/migrations/0001_initial.py` (Create model Profile)
  - `apps/user_settings/migrations/0001_initial.py` (Create model UserSettings)
- Executed `migrate` applying both migrations to remote Supabase PostgreSQL database:
  - `Applying profile.0001_initial... OK`
  - `Applying user_settings.0001_initial... OK`

---

## Verification Results
- **System Check**:
  ```bash
  venv\Scripts\python manage.py check
  System check identified no issues (0 silenced).
  ```
- **Migration Status**:
  ```bash
  venv\Scripts\python manage.py showmigrations
  profile
   [X] 0001_initial
  user_settings
   [X] 0001_initial
  ```
- **Test Suite**:
  ```bash
  venv\Scripts\python manage.py test apps.profile apps.user_settings --keepdb
  Ran 8 tests in 20.883s
  OK
  ```
