# 🔐 Automated CI Security Incident Management System

## 📌 Overview

This project demonstrates a DevSecOps automation workflow that integrates:

- GitHub Actions (CI/CD)
- Python automation
- Jira Cloud REST API (v3)
- Slack Incoming Webhooks

When a CI security scan detects a vulnerability, the system:

1. Automatically creates a structured Jira ticket
2. Sets severity and priority
3. Sends a real-time Slack notification to the IT Support team

This project simulates a production-grade automated incident response pipeline.

---

## 🏗 Architecture


Developer Push → GitHub Actions CI
        ↓
Security Scan Script
        ↓ (if failure)
Create Jira Incident
        ↓
Send Slack Alert to IT Channel



---

## 🚀 How It Works

### 1️⃣ Code Push
A developer pushes code to the GitHub repository.

### 2️⃣ CI Security Scan
GitHub Actions runs `security_scan.py`.

If a vulnerability is detected:
- Script exits with code `1`
- Workflow continues to Jira automation step

### 3️⃣ Jira Ticket Creation
`create_jira_ticket.py`:

- Calls Jira REST API `/rest/api/3/issue`
- Creates issue using Atlassian Document Format (ADF)
- Sets priority (e.g., High)
- Logs API response

### 4️⃣ Slack Notification
If Jira returns HTTP 201:

- Slack webhook sends formatted alert
- IT Support channel receives real-time notification

---

## 🛠 Technology Stack

- **GitHub Actions** – CI/CD automation
- **Python (requests library)** – API integration
- **Jira Cloud API v3** – Issue management
- **Slack Incoming Webhooks** – Real-time alerting
- **GitHub Secrets** – Secure credential storage

---

## 🔐 Security Best Practices Implemented

- No credentials stored in source code
- All secrets managed via GitHub Secrets
- HTTPS API communication
- Environment variable validation
- Structured JSON payload formatting
- Error handling and status logging

---

## 📂 Project Structure


.github/workflows/ci.yml
security_scan.py
create_jira_ticket.py
requirements.txt
README.md


---

## ⚙️ Environment Variables Required

Set these in GitHub → Settings → Secrets → Actions:

JIRA_URL
JIRA_EMAIL
JIRA_API_TOKEN
JIRA_PROJECT
SLACK_WEBHOOK


---

## 📊 Example Output

### Jira Ticket Created
- Issue Key: KAN-8
- Priority: High
- Status: IDEA

### Slack Notification
Channel: `#it-support-alerts`



---

## 📊 Example Output

### Jira Ticket Created
- Issue Key: KAN-8
- Priority: High
- Status: IDEA

### Slack Notification
Channel: `#it-support-alerts`


---

## 🎯 Business Impact

This automation:

- Eliminates manual incident reporting
- Reduces response time to zero
- Improves visibility for IT operations
- Ensures structured tracking of vulnerabilities
- Demonstrates production-style DevSecOps workflow

---

## 🔮 Future Enhancements

- CVSS severity scoring integration
- Auto-assignment in Jira
- SLA tracking fields
- Slack Block Kit rich formatting
- Scan log attachment to Jira
- Dashboard reporting
- SIEM integration

---

## 👨‍💻 Author

Muhammad Umair Ahsan  
DevOps / IT Automation Case Study  

---

## 📜 License

This project is for demonstration and educational purposes.


