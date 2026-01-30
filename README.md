Project Report: Cloud-Based Book Management
System
Yasin Selim Akay 97277
1. Project Overview
This project is a web-based "Book Management System" deployed on
Microsoft Azure. The application allows users to list, add, and delete book
records (CRUD operations). The primary goal was to demonstrate a fully
automated deployment pipeline (CI/CD) and cloud database integration.
2. Technology Stack
 Backend: Python with Flask framework.
 Database: Azure Database for PostgreSQL (Flexible Server).
 ORM: Flask-SQLAlchemy for database interactions.
 Deployment: Azure App Service (Linux).
 CI/CD: GitHub Actions for automated builds and deployments.
3. Implementation Steps
A. Database Configuration (Hard Requirement)
 A PostgreSQL Flexible Server was provisioned on Azure.
 To ensure security, the database connection string was not
hardcoded in the source code.
 The connection was established using an Environment Variable
named DATABASE_URL configured within the Azure App Service
settings.
B. Application Development & CRUD Operations
 The application features a clean UI with "Add" and "Delete"
functionalities.
 SQLAlchemy was used to define the Book model and manage the
database schema automatically.
 The frontend uses a responsive design inspired by modern UI
elements.
C. CI/CD Pipeline & Deployment
 The source code is hosted on GitHub.
 GitHub Actions was configured to trigger a deployment every time
a change is pushed to the main branch.
 This ensures that the application is always up-to-date without
manual intervention.
4. Security & Best Practices
 Environment Variables: Sensitive data like database credentials are
stored securely in Azure's "Environment Variables".
 SSL Connection: The database connection uses sslmode=require to
encrypt data in transit.
 Resource Management: Resources were grouped under a single
Resource Group (YasinFinalProject) for better management and
cost tracking.
5. Conclusion
The project successfully meets all the requirements. It is a live, scalable
web application backed by a cloud database and managed through a
professional DevOps workflow.
Live URL: https://yasin-bookcase-apphpcshzfmhyeed8cm.polandcentral-01.azurewebsites.net/
GitHub Repo: https://github.com/yasinselimakay/azure-final-project
