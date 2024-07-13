# Selenium Form Submission and Email Assignment

## Overview
This project automates the submission of a Google Form using Selenium, captures a screenshot of the confirmation page, and sends the screenshot via email using Django.

## Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your email settings in `settings.py`.
4. Run the Django server: `python manage.py runserver`.
5. Visit `http://127.0.0.1:8000/send-email/` to execute the script.

## Files
- `form_submission/selenium_script.py`: Selenium script for form submission.
- `form_submission/views.py`: Django view for sending email.
- `form_submission/templates/success.html`: Confirmation template.
