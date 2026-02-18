🧪 Clinical Trial Registry API
================================

A production-ready Django REST API for managing clinical trials with:

- JWT Authentication
- Role-Based Access Control (Admin / Researcher)
- Owner-only edit permissions
- Filtering, Search & Ordering
- Pagination
- PostgreSQL
- Swagger Documentation
- Docker Support
- Production Deployment Ready

------------------------------------------------------------
🚀 FEATURES
------------------------------------------------------------

🔐 JWT Authentication (SimpleJWT)
👥 Role-Based Access Control (Admin / Researcher)
🛡 Owner-Only Update/Delete Permissions
🔎 Filtering, Search & Ordering
📄 Pagination (PageNumberPagination)
🐘 PostgreSQL Database
📘 Swagger API Documentation (drf-spectacular)
🐳 Dockerized Setup
🌍 Production Deployment Ready

------------------------------------------------------------
🛠 TECH STACK
------------------------------------------------------------

- Python 3.10
- Django 4.2+
- Django REST Framework
- PostgreSQL
- SimpleJWT
- django-filter
- drf-spectacular
- Gunicorn
- Docker & Docker Compose

------------------------------------------------------------
📦 PROJECT STRUCTURE
------------------------------------------------------------

clinical_registry/
│
├── clinical_registry/   # Project settings
├── trials/              # Clinical trial app
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py

------------------------------------------------------------
⚙️ LOCAL DEVELOPMENT (WITHOUT DOCKER)
------------------------------------------------------------

1️⃣ Clone the repository

git clone https://github.com/Tanvirnawab/clinical-trial-api.git
cd clinical-trial-api

2️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate  (Windows)
source venv/bin/activate (Mac/Linux)

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Setup PostgreSQL database

Create a PostgreSQL database and update settings.py or .env with:

DB_NAME=clinical_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

5️⃣ Run migrations

python manage.py makemigrations
python manage.py migrate

6️⃣ Create superuser

python manage.py createsuperuser

7️⃣ Run server

python manage.py runserver

API will run at:
http://127.0.0.1:8000

Swagger docs:
http://127.0.0.1:8000/api/docs/

------------------------------------------------------------
🐳 RUN WITH DOCKER (RECOMMENDED)
------------------------------------------------------------

1️⃣ Build and run

docker-compose up --build

2️⃣ The app will:

- Run migrations automatically
- Create superuser (if configured)
- Start Gunicorn server

App URL:
http://localhost:8000

------------------------------------------------------------
🔐 AUTHENTICATION
------------------------------------------------------------

Obtain JWT token:

POST /api/token/

{
  "username": "yourusername",
  "password": "yourpassword"
}

Refresh token:

POST /api/token/refresh/

Use token in headers:

Authorization: Bearer <access_token>

------------------------------------------------------------
👥 ROLE-BASED ACCESS CONTROL
------------------------------------------------------------

Roles supported:

- Admin
- Researcher

Admin:
- Full access to all trials

Researcher:
- Can create trials
- Can edit/delete only their own trials
- Read-only access to others

Permissions are enforced via:
- Custom permission classes
- Owner-based validation

------------------------------------------------------------
🔎 FILTERING & SEARCH
------------------------------------------------------------

Filter by status:

/api/trials/?status=Approved

Search:

/api/trials/?search=diabetes

Ordering:

/api/trials/?ordering=created_at
/api/trials/?ordering=-created_at

------------------------------------------------------------
🌍 PRODUCTION DEPLOYMENT
------------------------------------------------------------

IMPORTANT: Never use DEBUG=True in production.

Set environment variables:

DEBUG=False
ALLOWED_HOSTS=yourdomain.com
SECRET_KEY=your_secret_key

------------------------------------------------------------
🚀 DEPLOY ON RENDER (Example)
------------------------------------------------------------

1️⃣ Push project to GitHub

2️⃣ Go to https://render.com

3️⃣ Create:
- Web Service (Docker)
- PostgreSQL database

4️⃣ Add environment variables in Render:

SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=your-render-domain.onrender.com
DATABASE_URL=your_postgres_connection_string

5️⃣ Render will automatically:
- Build Docker image
- Run migrations
- Start Gunicorn

------------------------------------------------------------
🛡 PRODUCTION CHECKLIST
------------------------------------------------------------

✔ DEBUG=False
✔ Strong SECRET_KEY
✔ PostgreSQL in production
✔ Allowed hosts configured
✔ HTTPS enabled
✔ Secure headers enabled

Optional improvements:

- Add Redis caching
- Add Celery for async tasks
- Add CI/CD pipeline
- Add automated tests

------------------------------------------------------------
📘 API DOCUMENTATION
------------------------------------------------------------

Swagger UI:
https://yourdomain.com/api/docs/

OpenAPI schema:
https://yourdomain.com/api/schema/

------------------------------------------------------------
👨‍💻 AUTHOR
------------------------------------------------------------

Tanvir Nawab

------------------------------------------------------------
⭐ FUTURE IMPROVEMENTS
------------------------------------------------------------

- Separate dashboards per role
- Email verification
- Audit logs
- Advanced trial analytics
- File uploads for documents

------------------------------------------------------------

✅ Production Ready
✅ Docker Ready
✅ PostgreSQL Ready
✅ JWT Secured
