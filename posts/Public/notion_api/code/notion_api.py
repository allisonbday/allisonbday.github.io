import requests
import json

SECRET = secret
DATABASE_ID = database_id
from datetime import datetime, timezone

# %%
headers = {
    "Authorization": "Bearer " + SECRET,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def get_database():
    base_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    page_size = 100

    payload = {
        "page_size": page_size,
        "filter": {
            "or": [
                {"property": "Status", "status": {"does_not_equal": "Done"}},
                {"property": "Tags", "multi_select": {"contains": "Improvement"}},
            ]
        },
        "sorts": [{"property": "Due", "direction": "ascending"}],
    }

    response = requests.post(base_url, json=payload, headers=headers)
    data = response.json()

    results = data["results"]
    while data["has_more"]:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        response = requests.post(base_url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results


from datetime import datetime, timezone


def patch_page():
    page_url = f"https://api.notion.com/v1/pages/{PAGE_ID}"

    payload = {
        "properties": {
            "Status": {"status": {"name": "Done"}},
            "Tags": {"multi_select": [{"name": "Improvement"}]},
            "Due": {
                "date": {
                    "start": datetime(2023, 1, 15).isoformat(),
                    "end": None,
                }
            },
            "Priority": {"select": {"name": "Not"}},
        }
    }

    response = requests.patch(page_url, json=payload, headers=headers)

    return response.json()


# %%
