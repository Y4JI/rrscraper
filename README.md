# Royal Road Scraper and Reading Tracker

This Django app imports fiction titles and recent release links from Royal Road’s official RSS feeds. Signed-in users share the local library and can save their own reading progress.

## Run locally on Windows

Run these commands in PowerShell from the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Open [the local dashboard](http://127.0.0.1:8000/). The app uses local SQLite when `DATABASE_URL` is unset.

## Import a novel

Paste its Royal Road fiction URL into the dashboard form. Run the import worker in a second PowerShell window from the project folder so it can process queued requests:

```powershell
.\.venv\Scripts\python.exe manage.py process_imports
```

RSS imports capture the title and recent releases. Follow a release link to read it on Royal Road. The dashboard reports downloaded chapter bodies independently of RSS releases. Use `process_imports --once` to drain the queue and exit. To retry a failed import, submit the fiction URL again. After stopping a worker that was interrupted during an active job, use `process_imports --recover-job JOB_ID --once` to return that job to the queue and process it.

The command line also supports RSS imports. Use the username of an existing local account.

```powershell
.\.venv\Scripts\python.exe manage.py import_novel "https://www.royalroad.com/fiction/139212/the-hundred-reigns-timeloop-litrpg" --username YOUR_USERNAME --rss
```

## Import full chapters from an author-provided export

Use a copy the author or rights holder has provided for local import. Downloaded chapters are available to signed-in users of this installation. Convert the export to a UTF-8 JSON file with the fiction ID, title, author, and chapter records. Each chapter needs its original Royal Road URL and a plain-text body. The IDs and URLs below are examples.

```json
{
  "royalroad_id": "12345",
  "title": "Example novel",
  "author_name": "Example author",
  "chapters": [
    {
      "chapter_number": 1,
      "title": "Opening chapter",
      "content": "The author's chapter text goes here.",
      "source_url": "https://www.royalroad.com/fiction/12345/example-novel/chapter/54321/opening-chapter"
    }
  ]
}
```

```powershell
.\.venv\Scripts\python.exe manage.py import_novel "https://www.royalroad.com/fiction/12345/example-novel" --username YOUR_USERNAME --author-export .\novel-export.json
```

The export import reads a local file and updates chapters by their Royal Road IDs. Downloaded chapters appear on the novel detail page and can be read inside the app. Live chapter-page requests for *The Hundred Reigns* returned HTTP 403 in this environment. An official RSS refresh can still update its release list.

## Hosting configuration

Set `DJANGO_ENV=production`, generate a private `DJANGO_SECRET_KEY` for the deployment, and set `DJANGO_ALLOWED_HOSTS` to the comma-separated hostnames you serve. Production mode enables secure cookies, HTTPS redirects and HSTS. Set `DJANGO_HSTS_INCLUDE_SUBDOMAINS=1` only if all subdomains support HTTPS. Enable `DJANGO_HSTS_PRELOAD=1` only if you intend to preload the domain.

Use a production WSGI or ASGI server and run the import worker separately. Run `python manage.py migrate`, `python manage.py collectstatic`, and `python manage.py check --deploy` before serving requests. Configure the host to serve collected files from `staticfiles/` and keep the runtime database and media in persistent storage. For PostgreSQL, set `DATABASE_URL`. SSL is required by default. `DATABASE_SSL_REQUIRE=0` allows a local PostgreSQL instance without SSL for testing.
