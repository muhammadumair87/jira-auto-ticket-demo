import os
import requests

JIRA_URL = os.environ["JIRA_URL"]
EMAIL = os.environ["JIRA_EMAIL"]
API_TOKEN = os.environ["JIRA_API_TOKEN"]
PROJECT_KEY = os.environ["JIRA_PROJECT"]

def create_ticket():
    url = f"{JIRA_URL}/rest/api/3/issue"

    auth = (EMAIL, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "project": {
                "key": PROJECT_KEY
            },
            "summary": "🚨 Security Vulnerability Detected via CI",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": "Automated CI scan detected a critical vulnerability."
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Task"
            }
        }
    }

    response = requests.post(url, json=payload, headers=headers, auth=auth)

    print("Status:", response.status_code)
    print(response.text)

create_ticket()