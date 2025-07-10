# Kanova CRM – Backend (Django)

This is the backend API for **Kanova CRM**, a lightweight CRM built to help small businesses manage their clients and interactions with ease.

---

##  Features

- **Client Management** – Track name, company, job title, contact info, and status
-  **Lifecycle & Status** – Categorize clients by lifecycle stage and custom status labels
-  **Interaction Notes** – Log notes, emails, calls, tasks, meetings, and more
-  **Reminders** – Set follow-up dates and descriptions
-  **RESTful API** – Ready to connect with any front-end app

---

##  Tech Stack

- Django + Django REST Framework
- SQLite (or PostgreSQL-ready)
- UUID for primary keys
- Simple structure: one `contact` app

---

##  Models Overview

```python
Client
├── name, email, phone, company
├── lifecycle_stage, status
├── created_at
│
├── [notes] → InteractionNote
├── [reminders] → Reminder

ClientStatus – label/status (e.g. New, Lead, Customer)

InteractionNote – type-based log (note, email, call, task, etc)

Reminder – follow-up date + description

