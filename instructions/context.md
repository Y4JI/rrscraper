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

---

## Instruction Hierarchy
- **Task & Architecture Requirements (Source of Truth)**: `CSIT327_Python_Django_Vertical_Slicing_and_Supabase_Guide.pdf`.
- **Pre-migration Baseline Reference**: `instructions/APP_STRUCTURE.md`.
- **Step-Specific Changes & History**: `instructions/CHANGES_STEP1.md`.
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

### Currently Working On:
- Transitioning to **Step 2: Supabase Integration**.

### Decisions Already Made:
- Project configuration folder is `config/` (matches guide).
- User features are organized strictly as vertical slices inside `apps/<feature>/`.
- Feature-specific templates live under `templates/<feature>/`.
- Feature-specific static assets live under `static/<type>/<feature>/`.
- Retained custom dark theme UI styling, responsive card designs, and form validation while strictly abiding by the guide's app boundaries.

### Known Bugs / Issues:
- None. System checks and runtime navigation are clean.

---

## Next Step: Step 2 — Integrate Supabase

Follow sections 10–14 of the guide:
1. **Install database packages**:
   ```bash
   pip install psycopg[binary] dj-database-url python-dotenv Pillow
   pip freeze > requirements.txt
   ```
2. **Ensure `.env` is ignored**: Verify `.env` is in `.gitignore`.
3. **Set up `.env`**: Prompt the user for (or add) their Supabase PostgreSQL connection string:
   ```env
   DATABASE_URL=postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@[POOLER-HOST]:5432/postgres
   ```
4. **Update `config/settings.py`**:
   - Import `dotenv` and `dj_database_url`.
   - Call `load_dotenv(BASE_DIR / ".env")`.
   - Configure `DATABASES` using `dj_database_url.parse(os.environ["DATABASE_URL"], conn_max_age=600, ssl_require=True)`.
5. **Run check and migrations**:
   - `python manage.py check`
   - `python manage.py migrate` (creates default auth/session tables in Supabase PostgreSQL).
6. **Subsequent steps to follow**:
   - Step 3: Implement `apps/profile` and `apps/user_settings` models, views, templates, static files, and migrations.
   - Step 4: Improve Home screen with links to Profile and Settings.
   - Step 5 & 6: Test and verify database rows in Supabase Table Editor.

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
