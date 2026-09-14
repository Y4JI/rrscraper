# Step 2: Supabase Integration Summary

## Overview
In accordance with sections 10–14 of the **CSIT327 Python Django Vertical Slicing and Supabase Guide**, PostgreSQL database support was integrated using `psycopg`, `dj-database-url`, and `python-dotenv`.

---

## Key Changes Made

### 1. Installed Database & Image Dependencies
Installed the required libraries into the virtual environment (`venv`):
- `psycopg[binary]`: PostgreSQL database adapter for Python/Django.
- `dj-database-url`: Utility to parse the `DATABASE_URL` connection string.
- `python-dotenv`: Environment variable loader from local `.env`.
- `Pillow`: Image processing library required for Django's `ImageField` (used in subsequent Profile model).
- Generated clean UTF-8 `requirements.txt`.

### 2. Environment Variables & Security
- Verified `.env` is ignored by Git in `.gitignore`.
- Created `.env.example` with clear instructions on Supabase PostgreSQL connection URI format (Session Pooler vs Direct).
- Initialized local `.env` with `DATABASE_URL=` key ready for database credentials.

### 3. Project Configuration (`config/settings.py`)
- Imported `os`, `load_dotenv` from `dotenv`, and `dj_database_url`.
- Configured `.env` loading:
  ```python
  BASE_DIR = Path(__file__).resolve().parent.parent
  load_dotenv(BASE_DIR / ".env")
  ```
- Configured `DATABASES` to parse `os.environ["DATABASE_URL"]` with `conn_max_age=600` and `ssl_require=True` when `DATABASE_URL` is set:
  ```python
  if os.environ.get("DATABASE_URL"):
      DATABASES = {
          "default": dj_database_url.parse(
              os.environ["DATABASE_URL"],
              conn_max_age=600,
              ssl_require=True,
          )
      }
  else:
      DATABASES = {
          "default": {
              "ENGINE": "django.db.backends.sqlite3",
              "NAME": BASE_DIR / "db.sqlite3",
          }
      }
  ```

---

## Verification Result
- Executed `python manage.py check`:
  ```
  System check identified no issues (0 silenced).
  ```
- Executed `python manage.py migrate`:
  ```
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
  Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying sessions.0001_initial... OK
  ```
- All standard Django auth, session, and administrative tables are now active in the remote Supabase database.

---

## Next Step
- Step 3: Implement `apps/profile` and `apps/user_settings` vertical slices (models, migrations, views, URLs, templates, static assets).

