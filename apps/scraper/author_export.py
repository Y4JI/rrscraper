import json
from pathlib import Path

from .royalroad import CHAPTER_PATH, RoyalRoadError, identify


MAX_EXPORT_BYTES = 10 * 1024 * 1024


def read_author_export(path, fiction_id):
    try:
        with Path(path).open("rb") as export:
            raw = export.read(MAX_EXPORT_BYTES + 1)
    except OSError as exc:
        raise RoyalRoadError("Could not read the author export file.") from exc
    if len(raw) > MAX_EXPORT_BYTES:
        raise RoyalRoadError("Author export exceeds the 10 MiB limit.")
    try:
        data = json.loads(raw.decode("utf-8-sig"))
    except (ValueError, RecursionError) as exc:
        raise RoyalRoadError("Author export must be valid UTF-8 JSON.") from exc
    if not isinstance(data, dict) or data.get("royalroad_id") != fiction_id:
        raise RoyalRoadError("The author export Royal Road ID must match the fiction URL.")

    metadata = {"title": text_field(data, "title", 255), "author_name": text_field(data, "author_name", 150)}
    records = data.get("chapters")
    if not isinstance(records, list) or not records:
        raise RoyalRoadError("The author export must provide at least one chapter.")

    chapters = {}
    for entry in records:
        if not isinstance(entry, dict):
            raise RoyalRoadError("Each author export chapter must be a JSON object.")
        source_url = text_field(entry, "source_url", 500)
        parent_id, chapter_id = identify(source_url, CHAPTER_PATH)
        if parent_id != fiction_id or chapter_id in chapters:
            raise RoyalRoadError("Chapter URLs must be unique and belong to the exported novel.")
        number = entry.get("chapter_number")
        if type(number) is not int or not 1 <= number <= 2_147_483_647:
            raise RoyalRoadError("Each author export chapter must have a valid chapter_number.")
        content = text_field(entry, "content", MAX_EXPORT_BYTES)
        chapters[chapter_id] = {
            "chapter_number": number,
            "title": text_field(entry, "title", 255),
            "content": content,
            "word_count": len(content.split()),
            "source_url": source_url,
        }
    return metadata, chapters


def text_field(record, key, max_length):
    value = record.get(key)
    if not isinstance(value, str) or not value.strip() or len(value) > max_length or "\0" in value:
        raise RoyalRoadError(f"Invalid {key} in the author export.")
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise RoyalRoadError(f"Invalid Unicode in the author export field {key}.") from exc
    return value.strip()
