import feedparser

def fetch_rss_feed(url: str) -> list:
    """
    Fetch and parse an RSS feed from the given URL.
    :param url: RSS feed URL.
    :return: A list of feed items, each containing 'title' and 'link'.
    """
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