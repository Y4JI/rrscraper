from datetime import timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urljoin
from xml.etree import ElementTree

from bs4 import BeautifulSoup

from .royalroad import CHAPTER_PATH, FICTION_PATH, SHORT_CHAPTER_PATH, RoyalRoadError, identify


def parse_feed(xml, fiction_id):
    try:
        channel = ElementTree.fromstring(xml).find("channel")
    except (ElementTree.ParseError, LookupError, UnicodeError) as exc:
        raise RoyalRoadError("Royal Road returned invalid RSS XML.") from exc
    title = channel.findtext("title", "").strip() if channel is not None else ""
    if not title or len(title) > 255:
        raise RoyalRoadError("The Royal Road feed did not provide a valid novel title.")
    releases = {}
    for item in channel.findall("item"):
        chapter_url = item.findtext("link", "").strip()
        chapter_title = item.findtext("title", "").strip().removeprefix(f"{title} - ")
        if not chapter_title or len(chapter_title) > 255 or len(chapter_url) > 500:
            continue
        try:
            chapter_id, = identify(chapter_url, SHORT_CHAPTER_PATH)
        except RoyalRoadError:
            try:
                parent_id, chapter_id = identify(chapter_url, CHAPTER_PATH)
            except RoyalRoadError:
                continue
            if parent_id != fiction_id:
                continue
        try:
            release_date = parsedate_to_datetime(item.findtext("pubDate", ""))
            if release_date.tzinfo is None:
                release_date = release_date.replace(tzinfo=timezone.utc)
        except (ValueError, OverflowError):
            release_date = None
        releases.setdefault(chapter_id, {
            "title": chapter_title, "source_url": chapter_url, "release_date": release_date,
        })
    return title, releases


def parse_fiction(html, url):
    fiction_id, = identify(url, FICTION_PATH)
    page = BeautifulSoup(html, "html.parser")
    title = page.select_one(".fic-header h1, h1[property='name']")
    author = page.select_one(".fic-header h4 a, [property='author'] [property='name']")
    title_text = title.get_text(" ", strip=True) if title else ""
    author_text = author.get_text(" ", strip=True) if author else ""
    if not title_text or not author_text or len(title_text) > 255 or len(author_text) > 150:
        raise RoyalRoadError("Could not find a valid fiction title and author on the page.")

    synopsis = page.select_one(".description")
    chapters = {}
    chapter_links = page.select("#chapters a[href], .chapter-row[data-url], .chapter-row a[href]")
    for link in chapter_links:
        chapter_url = urljoin(url, link.get("href") or link.get("data-url", ""))
        try:
            parent_id, chapter_id = identify(chapter_url, CHAPTER_PATH)
        except RoyalRoadError:
            continue
        if parent_id == fiction_id and len(chapter_url) <= 500:
            chapters.setdefault(chapter_id, chapter_url)

    return {
        "title": title_text,
        "author_name": author_text,
        "synopsis": synopsis.get_text("\n", strip=True) if synopsis else None,
        "source_url": url,
    }, chapters


def parse_chapter(html):
    page = BeautifulSoup(html, "html.parser")
    title = page.select_one(".fic-header h1") or page.select_one("h1")
    body = page.select_one(".chapter-content")
    if not title or not body:
        raise RoyalRoadError("Could not find the chapter title and body on the page.")
    for element in body.select("script, style, template, [hidden]"):
        element.decompose()
    for element in body.select("p, div, blockquote, li, h2, h3, h4, br"):
        element.insert_after("\n")
    content = "\n".join(line.strip() for line in body.get_text().splitlines() if line.strip())
    title_text = title.get_text(" ", strip=True)
    if not title_text or len(title_text) > 255 or not content:
        raise RoyalRoadError("The chapter page did not provide a valid title and body.")
    return title_text, content
