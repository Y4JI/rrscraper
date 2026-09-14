# Project Context & Handoff Document

## Project
- **Application Name**: `rrscraper` (Royal Road Scraper / Web Fiction Tracker)
- **Course**: CSIT327
- **Overall Purpose**: A web application built with Django for authenticated users to search, browse, and track web fiction novels and chapters from Royal Road, following an enterprise **Vertical Slicing (package-by-feature)** architecture and connecting to a hosted **Supabase PostgreSQL** database.
- **Key Technologies**: Python 3.11, Django 5.2, PostgreSQL (via Supabase), psycopg, dj-database-url, python-dotenv, HTML5, Vanilla CSS (custom dark theme), Vanilla JavaScript.

---

## Source Documents
- **`CSIT327_Python_Django_Vertical_Slicing_and_Supabase_Guide.pdf`** (in project root):
  - The authoritative course guide prepared by instructor Joemarie Amparo.
  - Contains architectural rules for vertical slicing, target folder structure, step-by-step implementation code, database configuration commands, and screenshot submission checklist.
  - *Must remain unchanged.*
- **`instructions/APP_STRUCTURE.md`**:
  - Documents the original/baseline folder structure prior to vertical slice refactoring.
- **`instructions/CHANGES_STEP1.md`**:
  - Detailed changelog of Step 1 (Vertical Slicing conversion), documenting directory renames, file moves, setting updates, and initial verification results.
- **`instructions/CHANGES_STEP2.md`**:
  - Detailed changelog of Step 2 (Supabase integration setup), documenting installed packages, environment variable configuration, and settings updates.

---

## Instruction Hierarchy
- **Task & Architecture Requirements (Source of Truth)**: `CSIT327_Python_Django_Vertical_Slicing_and_Supabase_Guide.pdf`.
- **Pre-migration Baseline Reference**: `instructions/APP_STRUCTURE.md`.
- **Step-Specific Changes & History**: `instructions/CHANGES_STEP1.md`, `instructions/CHANGES_STEP2.md`.
- **Current Execution State & Next Actions**: `instructions/context.md` (this file).

*Rule: Do not invent arbitrary requirements or external frameworks. Follow the exact procedures and models prescribed in the PDF guide.*

---

## Current Progress

### Completed:
- [x] **Step 1: Vertical Slicing Restructuring**
  - Renamed `project/` to `config/` (updated `manage.py`, `asgi.py`, `wsgi.py`, `settings.py`).
  - Created `apps/` package with `__init__.py`.
  - Extracted legacy `scraper/` monolith into three independent vertical slices:
    - `apps/login/`: views (`login_view`, `logout_view`), `urls.py`, `apps.py`, `models.py`, `admin.py`.
    - `apps/register/`: views (`register_view`), forms (`UserRegistrationForm`), `urls.py`, `apps.py`, `models.py`, `admin.py`.
    - `apps/home/`: views (`home_view`), `urls.py`, `apps.py`, `models.py`, `admin.py`.
  - Organized templates into feature subfolders: `templates/login/login.html`, `templates/register/register.html`, `templates/home/home.html`.
  - Organized static assets into feature subfolders:
    - CSS: `static/css/login/login.css`, `static/css/register/register.css`, `static/css/home/home.css`.
    - JS: `static/js/login/login.js`, `static/js/register/register.js`, `static/js/home/home.js`.
    - Images: `static/images/login/`, `static/images/register/`, `static/images/home/`.
  - Configured `config/settings.py` (`INSTALLED_APPS`, `TEMPLATES['DIRS']`, `STATICFILES_DIRS`, `LOGIN_URL`).
  - Deleted obsolete `scraper/` folder.
  - Verified system check (`python manage.py check` returned 0 issues).
  - Verified live development server run (`python manage.py runserver`), confirming login, register, and home screens load, authenticate, redirect, and serve static CSS/JS without errors.
- [x] **Step 2: Supabase Integration & Initial Migration**
  - Installed database dependencies: `psycopg[binary]`, `dj-database-url`, `python-dotenv`, `Pillow`.
  - Generated `requirements.txt`.
  - Verified `.env` is ignored by Git in `.gitignore`.
  - Created `.env.example` template with connection URI documentation.
  - Configured local `.env` with Supabase `DATABASE_URL`.
  - Updated `config/settings.py` to import `load_dotenv` and `dj_database_url`, load `.env`, and parse `DATABASE_URL` for PostgreSQL with connection pooling parameters (`conn_max_age=600`, `ssl_require=True`).
  - Ran `python manage.py check` (0 issues).
  - Successfully ran `python manage.py migrate` against Supabase PostgreSQL, applying all auth, admin, contenttypes, and session migrations.

### Currently Working On:
- Transitioning to **Step 3: Create Profile and Settings Features**.

### Decisions Already Made:
- Project configuration folder is `config/` (matches guide).
- User features are organized strictly as vertical slices inside `apps/<feature>/`.
- Feature-specific templates live under `templates/<feature>/`.
- Feature-specific static assets live under `static/<type>/<feature>/`.
- Retained custom dark theme UI styling, responsive card designs, and form validation while strictly abiding by the guide's app boundaries.
- `.env` holds the secret `DATABASE_URL` connection string and is excluded from source control.
- Supabase PostgreSQL is connected as the hosted database backend.

### Known Bugs / Issues:
- None. System checks and remote database migrations are clean.

---

## Next Step: Step 3 — Add Profile and Settings Data

Follow section 15 of the guide:
1. **Create feature apps**:
   ```bash
   python manage.py startapp profile apps/profile
   python manage.py startapp user_settings apps/user_settings
   ```
2. **Register apps in `config/settings.py`**:
   Add `'apps.profile'` and `'apps.user_settings'` to `INSTALLED_APPS`.
3. **Define Models**:
   - `apps/profile/models.py`: `Profile` model (`user`, `full_name`, `bio`, `profile_image`).
   - `apps/user_settings/models.py`: `UserSettings` model (`user`, `dark_mode`, `email_notifications`).
4. **Create and apply migrations to Supabase**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create views, URLs, templates, and static files** for `profile` and `user_settings`.
6. **Subsequent steps**:
   - Step 4: Improve Home screen with links to Profile and Settings.
   - Step 5 & 6: Test, create test data/admin, and verify rows in Supabase Table Editor.

---

## Important Constraints
- **Vertical Slicing Integrity**: Do not mix logic or assets between feature apps. Avoid cross-feature imports unless genuinely cross-cutting.
- **Folder Rule**:
  - Python/Django code: `apps/<feature>/`
  - HTML templates: `templates/<feature>/`
  - CSS / JS / Images: `static/css/<feature>/`, `static/js/<feature>/`, `static/images/<feature>/`
- **Secrets Management**: Never commit database passwords or `.env` to Git.
- **Database Scope**: Supabase is used as the hosted PostgreSQL database for Django. Do NOT replace Django authentication with Supabase Auth (Django's `User` model manages auth).
- **User Validation**: Ask for validation from the user before executing major or destructive operations.

---

## Instructions for a New Conversation
When starting a new conversation with this codebase:
1. Read `instructions/context.md` first to understand project state.
2. Read the referenced instruction files (`instructions/CHANGES_STEP1.md`, `instructions/APP_STRUCTURE.md`) before making structural changes.
3. Consult `CSIT327_Python_Django_Vertical_Slicing_and_Supabase_Guide.pdf` for exact instructor requirements, models, and submission criteria.
4. Inspect the existing codebase to verify the current state rather than making assumptions.
5. Continue from the documented progress (starting at **Next Step: Step 2 — Integrate Supabase**) rather than re-doing finished work.
6. Adhere strictly to the vertical slicing structure and constraints.
7. Update `instructions/context.md` whenever a major milestone/step is completed.
