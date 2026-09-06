# InsightGuard

## AI-Powered Insider Threat Investigation System

InsightGuard is a cybersecurity prototype designed to help security teams investigate suspicious employee activity.

The system analyzes access activity, calculates risk, and provides an AI-assisted investigation report explaining why an alert is suspicious, what evidence supports it, possible legitimate explanations, and what investigators should check next.

---

## Key Features

- Employee access monitoring
- Risk-based security alerts
- Suspicious activity detection
- AI-assisted incident investigation
- Evidence-based risk explanation
- Recommended investigation steps
- REST API using FastAPI
- Cloud Run deployment ready
- Gemini AI integration

---

## How It Works

```text
Employee / Access Activity
          |
          v
     Access Logs
          |
          v
   Risk Scoring Engine
          |
          v
      Risk Alert
          |
          v
   InsightGuard API
          |
          v
      Gemini AI
          |
          v
 Investigation Report
