import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["From"] = "emailkamu@gmail.com"
email["To"] = "target@gmail.com"
email["Subject"] = "Tes Email dari Python"
email.set_content("Halo! Ini email otomatis pakai Python.")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("emailkamu@gmail.com", "PASSWORD_APLIKASI")
server.send_message(email)
server.quit()

print("Email terkirim")
