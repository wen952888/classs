import feedparser

def fetch_rss_feed(url: str) -> list:
    feed = feedparser.parse(url)
    if feed.bozo:
        raise RuntimeError(f"Failed to parse RSS feed: {feed.bozo_exception}")

    items = []
    for entry in feed.entries:
        items.append({
            "title": entry.title,
            "link": entry.link,
        })
    return items