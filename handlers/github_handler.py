from handlers.connection_handler import fetch_data
from typing import List

def fetch_github_data() -> List[str]:
    # try to fetch commit messages from url
    url = "https://api.github.com/repos/highcharts/highcharts/commits"
    data = fetch_data(url)

    if data == ["Could not fetch data"]: 
        return data
    if not data:
        return []

    # Extract commit-related data from the response
    return [item.get("commit", {}).get("message", "No message") for item in data]
