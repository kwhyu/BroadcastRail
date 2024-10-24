import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Mengambil email dan password dari variabel lingkungan
sender_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
receiver_email = os.getenv("reciver")

# Membuat pesan
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "OIOIOIOIOIOIOIOIOIOIOIOOIIO"
body = "OIOIOIOIOIOIOIOIOIOIOIOIOIOIOIOIOIOIOOIOI"
message.attach(MIMEText(body, "plain"))

# Mengirim email melalui server SMTP
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.close()
    print("Email berhasil dikirim!")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
