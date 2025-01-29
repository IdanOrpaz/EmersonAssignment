from handlers.connection_handler import fetch_data
from typing import List

def fetch_stackoverflow_data() -> List[str]:
    # try to fetch titles from url
    url = "https://api.stackexchange.com/2.2/tags/highcharts/faq?site=stackoverflow"
    data = fetch_data(url)

    if not data or "items" not in data:
        return []

    # Extract titles from the response
    return [item.get("title", "") for item in data["items"]]