import smtplib
import os
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env (untuk pengembangan lokal)
load_dotenv()

# Mengambil konfigurasi dari variabel lingkungan
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT", 587))
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
receiver_email = os.getenv("RECIVER_ENMAIL")  # Ganti dengan alamat email penerima

def send_email():
    # Membuat pesan
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Contoh Broadcast Email"
    body = "Ini adalah contoh pesan broadcast email yang dikirim secara otomatis."
    message.attach(MIMEText(body, "plain"))

    # Mengirim email melalui server SMTP
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
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
