import re
from http.client import HTTPException
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, build_opener


FICTION_PATH = re.compile(r"/fiction/([0-9]{1,50})(?:/[\w-]+)?/?", re.ASCII)
RSS_PATH = re.compile(r"/fiction/syndication/([0-9]{1,50})/?")
SHORT_CHAPTER_PATH = re.compile(r"/fiction/chapter/([0-9]{1,50})/?")
CHAPTER_PATH = re.compile(
    r"/fiction/([0-9]{1,50})/[\w-]+/chapter/([0-9]{1,50})(?:/[\w-]+)?/?",
    re.ASCII,
)
MAX_PAGE_BYTES = 5 * 1024 * 1024


class RoyalRoadError(ValueError):
    pass


class TemporaryRoyalRoadError(RoyalRoadError):
    pass


def identify(url, pattern):
    try:
        parts = urlsplit(url)
    except ValueError as exc:
        raise RoyalRoadError("Invalid Royal Road URL.") from exc
    match = pattern.fullmatch(parts.path)
    if parts.scheme != "https" or parts.netloc.lower() not in {
        "www.royalroad.com", "royalroad.com"
    } or not match:
        raise RoyalRoadError("Expected an HTTPS Royal Road fiction or chapter URL.")
    return match.groups()


def canonical_fiction(url):
    fiction_id, = identify(url, FICTION_PATH)
    path = urlsplit(url).path.rstrip("/")
    canonical = f"https://www.royalroad.com{path}"
    if len(canonical) > 500:
        raise RoyalRoadError("The Royal Road fiction URL exceeds 500 characters.")
    return fiction_id, canonical


class RoyalRoadRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        path = urlsplit(req.full_url).path
        pattern = next(pattern for pattern in (CHAPTER_PATH, RSS_PATH, FICTION_PATH) if pattern.fullmatch(path))
        if identify(newurl, pattern) != identify(req.full_url, pattern):
            raise RoyalRoadError("Royal Road redirected to a different fiction or chapter.")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_page(url, pattern, content_types=("text/html",)):
    identify(url, pattern)
    opener = build_opener(RoyalRoadRedirects())
    opener.addheaders = [("User-Agent", "rrscraper/1.0")]
    try:
        with opener.open(url, timeout=15) as response:
            if response.headers.get_content_type() not in content_types:
                raise RoyalRoadError("Royal Road returned an unexpected content type.")
            page = response.read(MAX_PAGE_BYTES + 1)
    except HTTPError as exc:
        if exc.code in {408, 429, 500, 502, 503, 504}:
            raise TemporaryRoyalRoadError(f"Royal Road returned HTTP {exc.code} for {url}.") from exc
        raise RoyalRoadError(f"Royal Road returned HTTP {exc.code} for {url}.") from exc
    except (URLError, OSError, HTTPException) as exc:
        raise TemporaryRoyalRoadError(f"Could not fetch {url}: {exc}") from exc
    if len(page) > MAX_PAGE_BYTES:
        raise RoyalRoadError("Royal Road page exceeded the size limit.")
    return page
