import smtplib

from_addr = "Sentry <sentry@finc.com>"
subject = "Hello from Sentry server"

client = smtplib.SMTP("127.0.0.1")
header = "From: {from_addr}\nSubject: {subject}\n\n".format(from_addr=from_addr, subject=subject)
message = "{header}This is a test email using smtplib module.\n\n".format(header=header)

client.sendmail("sentry@finc.com", ["nguyen.son@finc.com"], message)
client.quit()