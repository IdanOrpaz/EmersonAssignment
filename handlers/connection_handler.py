import requests
from typing import Any, Dict

# Retrieve data from given URL
def fetch_data(url: str) -> Any:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None