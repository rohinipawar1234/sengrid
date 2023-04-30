from django.shortcuts import render

# Create your views here.

from django.core.mail import send_mail
send_mail('Hello', 'Are You free tonight,lets catch up', 'rohinipawar49363@gmail.com', ['sonapawar080@gmail.com'])
