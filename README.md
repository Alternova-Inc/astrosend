# AstroSend

A secure file and text sharing application built with Django and HTMX.

## Features

- Secure authentication via email verification codes
- Domain-based email restrictions
- No persistent sessions for enhanced security
- Modern, responsive UI
- Secure file uploads with size limits
- Character-limited encrypted messages

## Project Structure

```
astrosend/
│
├── apps/                     # Application directory
│   ├── __init__.py
│   ├── auth_app/            # Authentication application
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── dashboard/           # Dashboard application
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations/
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
│
├── templates/               # HTML templates
│   ├── base/               # Base templates and assets
│   │   ├── js/
│   │   │   └── csrf.js     # CSRF token handling
│   │   └── css/
│   │       ├── base.css    # Base styles
│   │       ├── forms.css   # Form styles
│   │       └── buttons.css # Button styles
│   │
│   ├── auth_app/          # Authentication templates
│   │   ├── js/
│   │   │   └── success.js # Success page JavaScript
│   │   ├── css/
│   │   │   └── auth.css   # Authentication styles
│   │   ├── code_form.html
│   │   ├── email_form.html
│   │   ├── login.html
│   │   └── success.html
│   │
│   ├── dashboard/         # Dashboard templates
│   │   ├── js/
│   │   │   └── send.js    # Send page JavaScript
│   │   ├── css/
│   │   │   └── send.css   # Send page styles
│   │   ├── base.html      # Dashboard base template
│   │   ├── send.html      # Send secret page
│   │   └── history.html   # History page
│   │
│   └── base.html          # Main base template
│
├── .env                    # Environment variables (not in git)
├── .env.example           # Environment variables template
├── manage.py              # Django management script
├── run.sh                 # Development server script
└── setup_domains.py       # Script to set up allowed domains
```

## Setup

1. Clone the repository

2. Install dependencies:
   ```bash
   conda activate astrosend
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` with your specific configuration:
   - Database settings
   - Email settings (Mailgun)
   - Django settings (secret key, debug mode, etc.)

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Set up allowed domains:
   ```bash
   python setup_domains.py
   ```

6. Run the development server:
   ```bash
   ./run.sh
   ```

## Environment Variables

The following environment variables need to be configured in your `.env` file:

### Django Settings
- `DJANGO_SECRET_KEY`: Your Django secret key
- `DJANGO_DEBUG`: Set to "True" for development, "False" for production
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts

### Database Settings
- `DB_ENGINE`: Database engine (default: django.db.backends.postgresql)
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host (default: localhost)
- `DB_PORT`: Database port (default: 5432)

### Email Settings (Mailgun)
- `EMAIL_BACKEND`: Email backend to use
- `EMAIL_HOST`: SMTP host (default: smtp.mailgun.org)
- `EMAIL_PORT`: SMTP port (default: 587)
- `EMAIL_USE_TLS`: Whether to use TLS (default: True)
- `MAILGUN_SMTP_USERNAME`: Your Mailgun SMTP username
- `MAILGUN_SMTP_PASSWORD`: Your Mailgun SMTP password
- `DEFAULT_FROM_EMAIL`: Default sender email address

## Security Considerations

- The application doesn't maintain persistent sessions for enhanced security
- Authentication codes expire after 10 minutes
- Only specific email domains are allowed
- PostgreSQL is used for robust data storage
- Environment variables are used for sensitive configuration
- The `.env` file is not committed to version control 