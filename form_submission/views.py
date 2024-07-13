# form_submission/views.py
from django.core.mail import EmailMessage
from django.shortcuts import render
from .selenium_script import submit_form

def send_email(request):
    screenshot_path = submit_form()

    # Compose the email content
    email_subject = 'Python (Selenium) Assignment - Himanshu Sharma'
    email_body = (
        'Dear Tech Team,\n\n'
        'I am pleased to submit my completed assignment for the Python (Selenium) role. Please find the attached files which include the source code, brief documentation, and the screenshot of the confirmation page.\n\n'
        'Additionally, here is the link to the GitHub repository containing my code:\n'
        'https://github.com/himanshu-sharmav/selenium_assignment\n\n'
        'Thank you for considering my application. I look forward to the next steps in the selection process.\n\n'
        'Best regards,\n'
        'Himanshu Sharma'
    )

    # Create the email
    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email='himanshu.2226cs1157@kiet.edu',
        to=['tech@themedius.ai'],
        cc=['hr@themedius.ai']
    )

    # Attach the screenshot
    email.attach_file(screenshot_path)
    email.attach_file('selenium_assignment.zip')
    email.attach_file('approach.md')

    # Send the email
    email.send()

    return render(request, 'success.html')
