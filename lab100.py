"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server. starttls()
#Next, log in to the server
server.login("thennavanpmohan@gmail.com", "gmail1943")

#Send the mail
msg = "helo "
server.sendmail("thennavanpmohan@gmail.com","siddharthmishra@example.com", msg)
server.quit()