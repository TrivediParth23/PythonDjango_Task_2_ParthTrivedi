# JWT Authentication App

This Django application implements JWT (JSON Web Token) authentication for user login and signup functionalities. It ensures secure user authentication in a RESTful API.

## Features
- User registration (signup) with email and password.
- JWT-based authentication for user login.
- Protected API endpoints requiring token authentication.
- Easy integration with front-end applications.

## Installation
1. Clone the repository.
2. Navigate to the project directory: `cd jwt_auth`
3. Install requirements: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Start the server: `python manage.py runserver`

## Usage
- Signup: POST request to `/api/accounts/signup/` with user credentials.
- Login: POST request to `/api/accounts/login/` to receive a JWT token.
- Access protected endpoints by including the token in the Authorization header: `Bearer <your_token>`.

## Note
Ensure to set `DEBUG=True` in `settings.py` for development purposes.
