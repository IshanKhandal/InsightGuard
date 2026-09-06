# InsightGuard

## AI-Powered Insider Threat Detection and Investigation Platform

InsightGuard is an AI-assisted cybersecurity platform designed to help security teams detect, prioritize, and investigate suspicious employee activity.

Modern organizations generate a large amount of security telemetry from employee logins, database access, file access, resource usage, and data transfers. The difficult part is not only identifying unusual behavior. Security analysts also need to understand **why an event is suspicious, what evidence supports the alert, whether there could be a legitimate explanation, and what should be investigated next**.

InsightGuard addresses this problem by combining a deterministic risk-analysis layer with an AI-powered investigation layer using **Google Gemini**.

The system transforms raw employee activity into an investigation workflow:

```text
Employee Activity
       |
       v
Access Logs
       |
       v
Risk / Anomaly Analysis
       |
       v
Risk Score
       |
       v
Security Alert
       |
       v
InsightGuard API
       |
       v
Google Gemini
       |
       v
AI Investigation Report
       |
       v
Human Security Analyst
```

The goal is not to replace a security analyst.

The goal is to reduce the time required to understand and investigate a suspicious event.

---

# 1. Problem Statement

Insider threats are difficult to identify because legitimate and malicious behavior can look similar.

For example, an employee accessing a sensitive database outside normal working hours could indicate:

* Unauthorized access
* Credential compromise
* Data exfiltration
* Privilege misuse
* A policy violation

However, the same activity could also be legitimate:

* Scheduled maintenance
* Emergency support
* Data migration
* Backup activity
* An authorized administrative task

A simple rule such as:

```text
Access after midnight = suspicious
```

creates too many false positives.

Similarly, a simple risk score such as:

```text
Risk Score = 87
```

does not explain the reasoning behind that score.

InsightGuard therefore separates the process into two stages:

```text
Stage 1
Detect and prioritize suspicious activity

Stage 2
Explain and investigate the alert using AI
```

---

# 2. Solution Overview

InsightGuard combines several components into a single investigation pipeline.

### Detection Layer

Processes employee access activity and identifies unusual behavior.

### Risk Layer

Produces a risk score based on available activity indicators.

### Alert Layer

Represents suspicious activity as a structured security alert.

### AI Investigation Layer

Sends the structured alert and investigator's question to Google Gemini.

### Human Review Layer

Allows a security analyst to review the AI-generated investigation before taking action.

This creates the following workflow:

```text
                ┌─────────────────────┐
                │ Employee Activity   │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ Access Log Data     │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ Risk Analysis       │
                │ & Scoring           │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ Security Alert      │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ FastAPI Backend     │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ Google Gemini       │
                │ AI Investigation    │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ Investigation       │
                │ Report              │
                └──────────┬──────────┘
                           |
                           v
                ┌─────────────────────┐
                │ Human Investigator  │
                └─────────────────────┘
```

---

# 3. Key Features

## 3.1 Employee Activity Monitoring

InsightGuard works with employee and access activity data.

The repository includes sample datasets:

```text
employees.csv
access_logs.csv
```

These datasets provide the activity context required by the backend and risk-analysis components.

---

## 3.2 Risk-Based Security Analysis

The system processes activity information and assigns risk-related information to employees and events.

Important contextual indicators can include:

* Employee identity
* Resource accessed
* Access time
* Amount of data transferred
* Previous alerts
* Existing risk score
* Historical activity

The purpose is to prioritize events that require investigation instead of treating every event equally.

---

## 3.3 Security Alerts

Suspicious activity is represented as structured alert information.

An example alert can look like:

```json
{
  "employee": "EMP-024",
  "risk_score": 87,
  "resource": "Payroll Database",
  "access_time": "02:13 AM",
  "data_transfer": "428 MB",
  "previous_alerts": 4
}
```

This structured format makes the alert usable by both traditional application logic and the AI investigation layer.

---

# 4. AI-Powered Investigation

The main AI capability of InsightGuard is its investigation endpoint.

Instead of simply asking Gemini to provide a generic explanation, the system supplies a structured security alert and a specific investigator question.

For example:

```text
Why is this alert considered high risk?
```

Gemini then generates an investigation report.

The report is designed to provide:

### Risk Explanation

Why the alert should receive attention.

### Evidence

Which specific alert attributes support the conclusion.

### Possible Legitimate Explanations

Reasons why the activity may not necessarily be malicious.

### Recommended Investigation Steps

What a security analyst should check next.

This creates a more useful workflow than simply displaying:

```text
HIGH RISK
```

---

# 5. Example Investigation

Consider the following alert:

```text
Employee:        EMP-024
Risk Score:      87
Resource:        Payroll Database
Access Time:     02:13 AM
Data Transfer:   428 MB
Previous Alerts: 4
```

An investigator asks:

```text
Why is this alert considered high risk?
```

InsightGuard sends the structured information to Gemini.

The resulting investigation identifies several contributing factors:

```text
High Risk Score
       +
Sensitive Resource
       +
Unusual Access Time
       +
Large Data Transfer
       +
Previous Alerts
       =
High Investigation Priority
```

The AI can then explain the evidence and suggest investigation steps such as:

* Verify the employee's role
* Confirm whether access was authorized
* Investigate the purpose of the data transfer
* Review previous alerts
* Check related database and network logs
* Determine whether the activity was scheduled
* Contact the employee or manager when appropriate

The system does not automatically assume malicious intent.

This is important because unusual behavior does not necessarily mean malicious behavior.

---

# 6. AI Investigation Principles

InsightGuard uses Gemini as an **investigation assistant**, not as an autonomous security decision-maker.

The AI investigation layer is designed around several principles.

## Evidence First

The model receives structured alert information as the basis for its analysis.

## No Invented Evidence

The AI should not create events, users, logs, or facts that were not supplied.

## Alternative Explanations

The system considers legitimate explanations for unusual behavior.

## Recommended Investigation

The AI provides suggested next steps rather than automatically taking irreversible actions.

## Human-in-the-Loop

Final decisions remain with the security investigator.

The overall philosophy is:

```text
AI assists investigation.
Human makes the decision.
```

---

# 7. Backend Architecture

InsightGuard uses a Python FastAPI backend.

The backend provides REST endpoints for:

* Employees
* Employee activity
* Risk scores
* Alerts
* Dashboard summaries
* Event ingestion
* AI investigation

The backend separates application responsibilities into different modules.

```text
                    FastAPI Application
                           |
        ┌──────────────────┼──────────────────┐
        |                  |                  |
        v                  v                  v
   API Routes        Risk Analysis      AI Service
        |                  |                  |
        v                  v                  v
    Schemas          Activity Data       Gemini API
        |
        v
   Database Layer
```

---

# 8. Project Structure

```text
InsightGuard/
│
├── main.py
│
├── database.py
│
├── models.py
│
├── schemas.py
│
├── realtime_scoring.py
│
├── seed_data.py
│
├── gemini_service.py
│
├── employees.csv
│
├── access_logs.csv
│
├── requirements.txt
│
├── Dockerfile
│
├── .gitignore
│
└── README.md
```

---

# 9. File-by-File Explanation

## `main.py`

Main FastAPI application.

It defines the application's API endpoints and connects the different backend components.

This is the primary entry point for the API server.

---

## `database.py`

Responsible for database configuration and SQLAlchemy connection management.

The application reads the database connection from the environment.

Example:

```text
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/DATABASE
```

For local development, SQLite can also be used.

---

## `models.py`

Contains SQLAlchemy database models.

The project architecture supports entities such as:

* Users / employees
* Access logs
* Security alerts

These models represent the structured security information used by the application.

---

## `schemas.py`

Contains Pydantic schemas used to validate API requests and responses.

This provides structured JSON contracts between the client and backend.

---

## `realtime_scoring.py`

Contains the activity/risk-scoring logic used to evaluate suspicious behavior.

The scoring layer is separate from the Gemini investigation layer.

This separation is intentional:

```text
Risk Engine
     |
     v
Detect suspicious activity

Gemini
     |
     v
Explain and investigate suspicious activity
```

---

## `seed_data.py`

Used to populate the local database using the supplied datasets.

It provides a reproducible way to initialize the prototype with sample employee and access activity.

---

## `gemini_service.py`

Contains the Google Gemini integration.

This module:

1. Loads the Gemini API credential from the environment.
2. Creates the Gemini client.
3. Receives structured security alerts.
4. Sends investigation instructions and alert context to Gemini.
5. Returns the generated investigation report.

The Gemini credential is not hardcoded in the source code.

---

# 10. REST API

InsightGuard exposes a REST API through FastAPI.

## Employee Endpoints

```text
GET /api/users
```

Returns monitored employees.

```text
GET /api/users/{user_id}/activity
```

Returns activity history for an employee.

```text
GET /api/users/{user_id}/risk-score
```

Returns the current risk information for an employee.

---

## Alert Endpoints

```text
GET /api/alerts
```

Returns security alerts.

```text
GET /api/alerts/{alert_id}
```

Returns details for a specific alert.

---

## Dashboard Endpoint

```text
GET /api/dashboard/summary
```

Returns aggregate information for the security dashboard.

---

## Event Ingestion

```text
POST /api/ingest
```

Allows a new activity event to be submitted to the system.

This is useful for demonstrating how the system can receive new activity during a live prototype demonstration.

---

# 11. AI Investigation API

## Endpoint

```text
POST /api/ai/investigate
```

This endpoint sends an alert to Gemini for investigation.

---

## Request

```json
{
  "alert": {
    "employee": "EMP-024",
    "risk_score": 87,
    "resource": "Payroll Database",
    "access_time": "02:13 AM",
    "data_transfer": "428 MB",
    "previous_alerts": 4
  },
  "question": "Why is this alert considered high risk?"
}
```

---

## Response

```json
{
  "analysis": "Investigation report generated by Gemini..."
}
```

The exact response is generated dynamically by Gemini.

---

# 12. API Documentation

FastAPI automatically provides an interactive Swagger interface.

Start the application:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

The documentation provides:

* Available endpoints
* Request schemas
* Response schemas
* Example requests
* Interactive API testing

This allows the complete backend to be demonstrated without writing additional client code.

---

# 13. Technology Stack

## Programming Language

**Python**

Used for the backend, API, data processing, database layer, and Gemini integration.

---

## Backend Framework

**FastAPI**

Used to build the REST API.

FastAPI provides:

* Request validation
* Automatic OpenAPI documentation
* JSON APIs
* High-performance ASGI support

---

## ASGI Server

**Uvicorn**

Used to run the FastAPI application.

---

## Database Layer

**SQLAlchemy**

Used as the ORM and database abstraction layer.

The architecture supports PostgreSQL and local SQLite development.

---

## AI

**Google Gemini**

Used for security-alert investigation and natural-language reasoning.

---

## Google GenAI SDK

The official Google GenAI Python SDK is used by the backend to communicate with Gemini.

---

## Containerization

**Docker**

The application is packaged as a container so that the same application can be executed locally and deployed to Google Cloud Run.

---

## Cloud Deployment

**Google Cloud Run**

Used as the target serverless container platform.

---

## Build Infrastructure

**Google Cloud Build**

Used to build the application container during source-based Cloud Run deployment.

---

## Container Registry

**Artifact Registry**

Used to store the container image generated for deployment.

---

# 14. Local Setup

## Requirements

Install:

* Python 3
* pip
* Git

For database-backed development, PostgreSQL can also be used.

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/IshanKhandal/InsightGuard.git
cd InsightGuard
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3: Configure Environment Variables

Create:

```text
.env
```

Add:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

For PostgreSQL:

```text
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/DATABASE
```

For local SQLite:

```text
DATABASE_URL=sqlite:///./insightguard.db
```

Do not commit `.env` to Git.

---

## Step 4: Start the Backend

```bash
uvicorn main:app --reload
```

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## Step 5: Open API Documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

---

# 15. Database Setup

The original backend architecture uses PostgreSQL for persistent storage.

A PostgreSQL database can be created using:

```bash
createdb insider_threat_db
```

Then configure:

```text
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/insider_threat_db
```

Run the seed script:

```bash
python seed_data.py
```

The seed script loads the available employee and access-log datasets into the database.

For quick local testing, SQLite can be used instead.

---

# 16. Environment Configuration

The application uses environment variables for configuration.

Example:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

DATABASE_URL=sqlite:///./insightguard.db
```

The application should never contain:

```python
api_key = "actual-secret-key"
```

Instead, the application loads credentials from the environment.

---

# 17. Security

Security is especially important because InsightGuard processes employee activity and potentially sensitive security information.

## API Key Security

Gemini credentials are stored through environment variables.

The `.env` file is excluded from version control.

---

## Database Credential Security

Database credentials are supplied using `DATABASE_URL`.

Credentials should not be embedded directly in Python source files.

---

## AI Safety

Gemini is used as an analysis layer.

The system does not grant Gemini direct control over:

* Employee accounts
* Databases
* Network infrastructure
* Access permissions
* Destructive operations

The AI produces an investigation report.

A human investigator remains responsible for operational decisions.

---

## Input Validation

FastAPI/Pydantic validates structured API requests.

Malformed requests are rejected instead of being passed directly into the application logic.

---

# 18. Firebase and Firestore Architecture

The current prototype uses the SQLAlchemy database architecture.

Firebase Authentication and Firestore are planned extensions for a cloud-native production architecture.

A production version can use:

```text
Firebase Authentication
          |
          v
Authenticated Investigator
          |
          v
InsightGuard API
          |
          v
Firestore
          |
          v
Investigation History
```

Firestore could store:

* Investigation records
* Alert metadata
* Analyst notes
* Investigation status
* Audit information

Firebase Authentication could provide:

* Google Sign-In
* User identity
* Authenticated sessions
* Role-based access

The current repository does not claim that Firestore is already the active database.

---

# 19. Cloud Run Deployment

InsightGuard includes a Dockerfile for containerized deployment.

The intended deployment architecture is:

```text
GitHub Repository
       |
       v
Google Cloud Build
       |
       v
Container Image
       |
       v
Artifact Registry
       |
       v
Cloud Run
       |
       v
Public HTTPS Endpoint
```

---

# 20. Docker

The Dockerfile packages the FastAPI application into a container.

The container:

1. Starts from a Python runtime
2. Installs dependencies
3. Copies the application
4. Exposes the Cloud Run port
5. Starts Uvicorn

The application listens on:

```text
0.0.0.0
```

and uses the Cloud Run `PORT` environment variable.

---

# 21. Cloud Run Command

The application can be deployed using:

```bash
gcloud run deploy insightguard \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated
```

The deployed service can then expose the FastAPI application through a public HTTPS endpoint.

For a production deployment, authentication and access restrictions should be configured according to the application's security requirements.

---

# 22. Cloud Run Environment Variables

The Gemini API key should be configured on Cloud Run rather than being stored inside the container image.

Example environment variable:

```text
GEMINI_API_KEY
```

For production deployments, Google Cloud Secret Manager can be used instead of directly storing sensitive values as ordinary environment variables.

---

# 23. Deployment Architecture

```text
                         Internet
                            |
                            v
                  ┌──────────────────┐
                  │   Cloud Run      │
                  │   InsightGuard   │
                  └────────┬─────────┘
                           |
              ┌────────────┼─────────────┐
              |            |             |
              v            v             v
        FastAPI API   Risk Engine    Gemini API
              |            |             |
              |            v             |
              |       Security Alert     |
              |                          |
              └──────────────┬───────────┘
                             v
                    Investigation Report
                             |
                             v
                    Security Investigator
```

---

# 24. Cloud-Native Expansion

The architecture can be expanded into a fully Google Cloud-native security platform.

A future architecture can look like:

```text
Employees / Systems
        |
        v
Event Ingestion
        |
        v
Cloud Services
        |
        v
Risk Analysis
        |
        v
Firestore
        |
        v
Cloud Run API
        |
        +----------------+
        |                |
        v                v
     Gemini        Firebase Auth
        |
        v
AI Investigation
        |
        v
Security Dashboard
```

This allows the prototype to evolve from a local demonstration into a scalable cloud application.

---

# 25. Error Handling

The FastAPI application uses HTTP response codes to communicate API results.

For example:

```text
200 OK
```

indicates a successful request.

Invalid request payloads can return:

```text
422 Unprocessable Entity
```

This is particularly useful for the AI investigation endpoint because the alert structure must contain valid fields before being sent to the AI layer.

---

# 26. Human-in-the-Loop Security Workflow

InsightGuard intentionally avoids treating AI output as an automatic security decision.

The recommended workflow is:

```text
Suspicious Activity
        |
        v
Risk Assessment
        |
        v
Alert Generated
        |
        v
AI Investigation
        |
        v
Evidence & Explanation
        |
        v
Human Review
        |
        v
Security Decision
```

This design helps prevent a generative AI model from independently making potentially harmful operational decisions.

---

# 27. Example End-to-End Scenario

Imagine an employee account accesses a payroll database at 2:13 AM.

The event contains:

```text
Employee       EMP-024
Resource       Payroll Database
Time           02:13 AM
Data Transfer  428 MB
Risk Score     87
Previous Alerts 4
```

### Detection

The activity is identified as high priority because multiple indicators appear together.

### Alert

InsightGuard represents the event as a structured alert.

### Investigation

A security analyst submits:

```text
Why is this alert considered high risk?
```

### AI Analysis

Gemini analyzes the supplied information.

### Result

The report identifies:

* High risk score
* Sensitive resource
* Unusual access time
* Large data transfer
* Repeated previous alerts

The AI then considers possible legitimate explanations and recommends what the investigator should verify.

### Human Decision

The investigator checks the relevant logs, employee role, authorization, and context before taking action.

---

# 28. Why AI Is Useful Here

Traditional security systems are good at identifying patterns.

However, investigators often need contextual explanations.

For example:

```text
Rule-Based System:

Risk Score = 87
```

versus:

```text
AI-Assisted Investigation:

The alert combines access to a sensitive payroll resource,
unusual access timing, a large data transfer, and repeated
previous alerts. These factors collectively increase the
priority of the investigation.

Possible legitimate explanations should still be checked
before concluding that the activity is malicious.
```

The second output is more useful to a human investigator because it provides context and next steps.

---

# 29. Design Philosophy

InsightGuard follows four principles.

## Detect

Identify potentially suspicious behavior.

## Prioritize

Use risk information to determine which activity deserves attention.

## Explain

Use Gemini to convert structured security signals into an understandable investigation report.

## Assist

Help a human investigator make a better-informed decision.

```text
DETECT
   ↓
PRIORITIZE
   ↓
EXPLAIN
   ↓
INVESTIGATE
   ↓
DECIDE
```

---

# 30. Current Implementation Status

## Implemented

* FastAPI backend
* Employee data handling
* Access log processing
* Database abstraction using SQLAlchemy
* Risk scoring architecture
* Security alert APIs
* Dashboard summary API
* Event ingestion API
* Gemini integration
* AI investigation endpoint
* Structured AI investigation requests
* AI-generated investigation reports
* Environment-based API key configuration
* Docker configuration
* Cloud Run deployment configuration
* Local development environment

## Planned / Production Extensions

* Firebase Authentication
* Firestore persistence
* Role-based access control
* Production security dashboard
* Real-time event streaming
* Investigation history
* Analyst notes
* Audit logging
* Secret Manager integration
* Advanced anomaly detection
* Production monitoring

---

# 31. Limitations

This project is a prototype intended to demonstrate the architecture and workflow of an AI-assisted insider-threat investigation system.

The sample datasets are not representative of every enterprise environment.

The AI investigation output should be treated as decision support and should be reviewed by a qualified security analyst.

The current implementation does not claim to automatically determine malicious intent.

---

# 32. Future Roadmap

### Phase 1 — Prototype

* Access logs
* Risk scoring
* Alerts
* Gemini investigation
* REST API
* Docker

### Phase 2 — Cloud

* Cloud Run
* Firestore
* Firebase Authentication
* Secret Manager
* Cloud monitoring

### Phase 3 — Security Operations

* Real-time event ingestion
* Alert queues
* Analyst workflows
* Investigation history
* Audit logs

### Phase 4 — Intelligence

* Behavioral baselines
* Advanced anomaly detection
* Employee risk profiles
* Correlation across multiple events
* Threat intelligence integration

---

# 33. Project Repository

GitHub:

https://github.com/IshanKhandal/InsightGuard

---

# 34. Challenge Context

InsightGuard was developed as a cybersecurity-focused AI application for the Google Cloud / Hack2skill Gen AI Academy APAC challenge.

The project demonstrates how Google Gemini can be incorporated into an existing application rather than being used only as a standalone chatbot.

The AI layer is integrated into a practical security workflow:

```text
Existing Security Data
        |
        v
Existing Risk Analysis
        |
        v
Existing Security Alert
        |
        v
Gemini Investigation
        |
        v
Actionable Investigation Context
```

The key idea is to use generative AI where it provides the most value:

**turning security signals into investigation context.**

---

# 35. Submission Summary

InsightGuard demonstrates an AI-assisted insider-threat investigation workflow combining:

* Python
* FastAPI
* SQLAlchemy
* Risk analysis
* Google Gemini
* Google GenAI SDK
* Docker
* Google Cloud Run

The system is designed around a human-in-the-loop security model where AI assists analysts with investigation and explanation while humans retain control over security decisions.

---

# 36. License

This project is provided as a prototype for demonstration and educational purposes.
