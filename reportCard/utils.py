import time
from django.core.mail import send_mail
from django.conf import settings

def run_func():
  print("Started")

  time.sleep(2)
  print("Executed")



def send_email_to_client():
  subject = "Test mail from django server"
  message = "Hi! test mail is sent"
  from_email = settings.EMAIL_HOST_USER
  recipient_list = ["sayaliambure15@gmail.com"]

  send_mail(subject, message, from_email, recipient_list)