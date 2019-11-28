#!/usr/bin/python

import smtplib

sender = 'info@finc.com'
receivers = ['nguyen.son@finc.com']

message = """From: No Reply <info@finc.com>
To: Son Nguyen <nguyen.son@finc.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('mailcatcher', 1025)
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
