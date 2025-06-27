# Django Healthcare Backend API

This project is a secure and modular backend system for a healthcare application, developed using **Django**, **Django REST Framework**, **PostgreSQL**, and **JWT Authentication**.

---

## Features

- User registration and login with JWT tokens
- Full CRUD operations for:
  - Patients
  - Doctors
  - Patient-Doctor mappings
- Only authenticated users can manage patient and doctor records
- Each patient is linked to the user who created them
- Patients can be assigned multiple doctors

---

## Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt

## pip install -r requirements.txt


---

## Authentication

JWT is used for secure authentication.

## /api/auth/register/
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}

## POST /api/auth/login/
{
  "email": "your_email@example.com",
  "password": "your_password"
}

## POST /api/patients/
{
  "name": "John Doe",
  "age": 35,
  "medical_history": "Diabetes and hypertension"
}
## PUT /api/patients/<id>/
{
  "name": "Updated Name",
  "age": 40,
  "medical_history": "Updated notes"
}

## POST /api/doctors/
{
  "name": "Dr. Smith",
  "specialization": "Cardiologist"
}
 ## PUT /api/doctors/<id>/
 {
  "name": "Dr. Smith Updated",
  "specialization": "Neurologist"
}

## POST /api/mappings/
{
  "patient": 1,
  "doctor": 2
}

## GET /api/mappings/<patient_id>/
## DELETE /api/mappings/<mapping_id>/
