HelloWorld is a simple web app that displays a greeting.

# Tech Stack

- Django
- Tailwind CSS

# Routing

The app responds to routes:
 - /: the hello page
 - /status: the system status page
 - /demo: the DB demo page

# Hello Page

A nice looking HTML page with the message: "Hello from CodeSpeak!"
- a button underneath the message saying "Greet"
  - on click, a JS alert dialog with the same message

In the footer, there is a link to the system status page.

# System Status Page

Display system status information:
- OS name and version
- Current date and time
- CPU usage
- Memory usage

# DB Demo page

Use the Demo table in the DB with fields:
- name
- description

A table displaying all records.
Below: edit boxes for each field and an "Add" button.

# Django Settings & Deployment

Read ALLOWED_HOSTS from an env variable $ALLOWED_HOSTS 
- format: comma-sperarated

Read CSRF_TRUSTED_ORIGINS from an env variable $CSRF_TRUSTED_ORIGINS
- format: comma-sperarated

Use `dj_database_url` to load DATABASE_URL from an environment variable if available