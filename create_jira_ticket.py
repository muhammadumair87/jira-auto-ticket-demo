import os
import requests

JIRA_URL = os.environ["JIRA_URL"]
EMAIL = os.environ["JIRA_EMAIL"]
API_TOKEN = os.environ["JIRA_API_TOKEN"]
PROJECT_KEY = os.environ["JIRA_PROJECT"]
SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK")

def create_ticket():
    url = f"{JIRA_URL}/rest/api/3/issue"
    auth = (EMAIL, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Simulated severity (for case study demo)
    priority = "High"

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
            },
            "priority": {
                "name": priority
            }
        }
    }

    response = requests.post(url, json=payload, headers=headers, auth=auth)

    print("Status:", response.status_code)
    print(response.text)

    # 🔔 Slack Notification if Ticket Created
    if response.status_code == 201:
        issue_key = response.json()["key"]
        jira_link = f"{JIRA_URL}/browse/{issue_key}"

        if SLACK_WEBHOOK:
            slack_message = {
                "text": f"""
🚨 *Security Vulnerability Detected*

• Ticket: {issue_key}
• Severity: {priority}
• Project: {PROJECT_KEY}

🔗 View in Jira:
{jira_link}

Assigned to: IT Support Team
"""
            }

            slack_response = requests.post(SLACK_WEBHOOK, json=slack_message)

            print("Slack notification sent.")
            print("Slack status:", slack_response.status_code)
        else:
            print("Slack webhook not configured.")

create_ticket()