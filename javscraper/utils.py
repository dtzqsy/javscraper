import cloudscraper

from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

__all__ = ["SCRAPER", "JAVResult", "perform_request"]

# Global scraper without needing to make a new instance per request
SCRAPER = cloudscraper.create_scraper(
    # Make sure mobile pages are not served
    browser={
        "custom": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.121 Safari/537.36"
    }
)


@dataclass
class JAVResult:
    """Results returned for a site"""
    name: str
    code: str
    studio: str
    image: str
    actresses: List[str]
    genres: List[str]
    release_date: datetime
    sample_video: Optional[str] = None
    description: Optional[str] = None


def perform_request(method: str, url: str, *args, **kwargs):
    """
    Creates a request with cloudscraper to avoid being stopped by cloudflare
    :param method: HTTP Method
    :param url: HTTP URL
    :param args: args to pass into cloudscraper
    :param kwargs: kwargs to pass into cloudscraper
    :return:
    """
    return SCRAPER.request(method, url, *args, **kwargs)
