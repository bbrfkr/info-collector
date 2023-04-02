from datetime import timedelta

import feedparser
from requests import post

from .settings import redis_client, rss_configs


def post_rss_feeds():
    for config in rss_configs:
        feed_url = config["feed_url"]
        webhook_url = config["webhook_url"]

        result = feedparser.parse(feed_url)
        feeds = result["entries"]
        for feed in feeds:
            title = feed["title"]
            link = feed["link"]

            if not redis_client.get(link):
                post(webhook_url, json={"content": f"{title}: {link}"})
                redis_client.set(link, title, ex=timedelta(days=30))
