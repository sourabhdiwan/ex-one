import requests

def fetch_gitlab_data(endpoint, headers):
    url = f"https://gitlab.com/api/v4/{endpoint}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
