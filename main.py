import smtplib
import os
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env (opsional, untuk pengembangan lokal)
load_dotenv()

# Mengambil email dan password dari variabel lingkungan
sender_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
receiver_email = os.getenv("reciver")

def send_email():
    # Membuat pesan
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "OIOIOIOIOI"
    body = "OIOIOIOIOIOIOI"
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

# Menjadwalkan pengiriman email setiap 1 menit
schedule.every(1).minutes.do(send_email)

# Looping untuk menjalankan tugas yang dijadwalkan
while True:
    schedule.run_pending()
    time.sleep(1)
