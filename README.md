# Employee Operations Platform

A full-stack employee operations platform for managing employees, departments, attendance, leave requests, tasks, and internal workflows.

Built with **React, TypeScript, Django REST Framework, and PostgreSQL**.

## 🚀 Project Status

> 🚧 Currently under development.

## ✨ Planned Features

* 🔐 Authentication and role-based access control
* 👥 Employee and department management
* 🕐 Employee attendance tracking
* 🏖️ Leave requests and approval workflows
* ✅ Task assignment and management
* 💬 Task comments
* 🔔 Notifications
* 📊 Admin, manager, and employee dashboards
* 📈 Attendance and task reports
* 📎 File attachments
* 📝 Audit logs

## 👤 User Roles

### Admin

* Manage employees and departments
* View company-wide attendance
* Manage tasks
* View reports
* Manage system settings

### Manager

* Manage team members
* Assign and manage tasks
* Review team attendance
* Approve or reject leave requests
* View team reports

### Employee

* View and update profile
* Check in and check out
* View attendance history
* Apply for leave
* View assigned tasks
* Update task status
* Comment on tasks

## 🛠️ Tech Stack

### Frontend

* React
* TypeScript
* TanStack Query
* React Hook Form
* Zod
* Tailwind CSS

### Backend

* Python
* Django
* Django REST Framework
* PostgreSQL
* JWT Authentication

### Planned Infrastructure

* Redis
* Celery
* Django Channels
* Docker
* AWS
* S3-compatible object storage

## 🏗️ Architecture

```text
React / TypeScript
        │
        │ REST API
        ▼
Django REST Framework
        │
        ▼
   PostgreSQL

Future:
        │
   ┌────┴────┐
   ▼         ▼
 Redis     Celery
```

## 📁 Project Structure

```text
employee-operations/
│
├── backend/
│   ├── config/
│   ├── users/
│   ├── departments/
│   ├── attendance/
│   ├── leaves/
│   ├── tasks/
│   ├── notifications/
│   ├── reports/
│   └── manage.py
│
├── frontend/
│
├── docs/
│   ├── architecture.md
│   ├── database.md
│   └── api.md
│
├── .gitignore
└── README.md
```

## 🔑 Authentication

The application will use JWT-based authentication with separate access and refresh tokens.

Protected API endpoints will enforce permissions based on the user's role and organizational relationships.

## 🗄️ Database

PostgreSQL will be used as the primary relational database.

Core entities include:

```text
User
Department
Attendance
LeaveRequest
LeaveBalance
Task
TaskComment
Notification
AuditLog
```

## 🧪 Testing

Automated tests will be added for:

* API endpoints
* Authentication and permissions
* Business rules
* Database operations
* React components and features

## 🚀 Deployment

Planned production architecture:

```text
Frontend  → Vercel
Backend   → AWS
Database  → PostgreSQL / AWS RDS
Files     → S3
Redis     → Managed Redis
```

## 📚 Documentation

Detailed technical documentation will be added as the project develops.

* [Architecture](docs/architecture.md)
* [Database Design](docs/database.md)
* [API Documentation](docs/api.md)

## 📌 Purpose

This project is being developed as a production-style full-stack application to explore practical software engineering concepts including API design, database modeling, authentication, authorization, business workflows, asynchronous processing, testing, and deployment.
