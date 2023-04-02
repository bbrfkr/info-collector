import os

import redis
import yaml

with open("config.yaml") as file:
    config = yaml.safe_load(file)

rss_configs = config["rss_configs"]

connpass_api_url = config["connpass_api_url"]
connpass_configs = config["connpass_configs"]

redis_client = redis.Redis(
    os.getenv("REDIS_HOST", "localhost"),
    os.getenv("REDIS_PORT", 6379),
    os.getenv("REDIS_DB", 0),
)
