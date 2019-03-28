# gmail settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


#sendgrid settings
EMAIL_HOST = 'smtp.krdia hoa' \
             '.net'
EMAIL_HOST_USER = 'yourusername@youremail.com'
EMAIL_HOST_PASSWORD = 'your password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


DEFAULT_FROM_EMAIL = 'Your Name <you@email.com>'
ADMINS = (
    ('You', 'you@email.com'),
)

MANAGERS = ADMINS




from django.conf import settings
from django.core.mail import send_mail

subject = 'Some subject'
from_email = settings.DEFAULT_FROM_EMAIL
message = 'This is my test message'
recipient_list = ['mytest@gmail.com', 'you@email.com']
html_message = '<h1>This is my HTML test</h1>'


send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)