# AstroSend

A secure file and text sharing application built with Django and HTMX.

## Features

- Secure authentication via email verification codes
- Domain-based email restrictions
- No persistent sessions for enhanced security
- Modern, responsive UI

## Project Structure

```
astrosend/
│
├── apps/                     # Application directory
│   ├── __init__.py
│   └── auth_app/             # Authentication application
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations/
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
│
├── astrosend/                # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/                   # Static files
│   └── css/
│       └── styles.css
│
├── templates/                # HTML templates
│   ├── auth_app/
│   │   ├── code_form.html
│   │   ├── email_form.html
│   │   ├── login.html
│   │   └── success.html
│   └── base.html
│
├── manage.py                 # Django management script
├── run.sh                    # Development server script
└── setup_domains.py          # Script to set up allowed domains
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   conda activate astrosend
   pip install django psycopg2-binary
   ```

3. Set up the database:
   ```
   python manage.py migrate
   ```

4. Set up allowed domains:
   ```
   python setup_domains.py
   ```

5. Run the development server:
   ```
   ./run.sh
   ```

## Email Configuration

For development, emails are output to the console. In production, configure Mailgun SMTP settings in `settings.py` or using environment variables:

- `MAILGUN_SMTP_USERNAME`
- `MAILGUN_SMTP_PASSWORD`
- `DEFAULT_FROM_EMAIL`

## Security Considerations

- The application doesn't maintain persistent sessions for enhanced security
- Authentication codes expire after 10 minutes
- Only specific email domains are allowed
- PostgreSQL is used for robust data storage 