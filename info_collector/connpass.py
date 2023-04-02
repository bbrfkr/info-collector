from datetime import date, timedelta

from requests import get, post

from .settings import connpass_api_url, connpass_configs, redis_client


def post_connpass_events():
    today = date.today()
    this_month = today.replace(day=1)
    after_one_month = (this_month + timedelta(days=32)).replace(day=1)
    after_two_month = (after_one_month + timedelta(days=32)).replace(day=1)
    month_format = "%Y%m"

    for config in connpass_configs:
        keyword = config["keyword"]
        webhook_url = config["webhook_url"]

        params = {
            "keyword": keyword,
            "ym": [this_month, after_one_month, after_two_month],
            "order": 3,
        }

        response = get(connpass_api_url, params=params)
        events = response.json()["events"]
        for event in events:
            title = event["title"]
            event_url = event["event_url"]
            if not redis_client.get(event_url):
                post(webhook_url, json={"content": f"{title}: {event_url}"})
                redis_client.set(event_url, title, ex=timedelta(days=90))


post_connpass_events()