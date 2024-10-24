import os
import schedule
import time
import requests
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env (untuk pengembangan lokal)
load_dotenv()

# Mengambil konfigurasi dari variabel lingkungan
mailgun_api_key = os.getenv("MAILGUN_API_KEY")
mailgun_domain = os.getenv("MAILGUN_DOMAIN")
sender_email = os.getenv("SENDER_EMAIL")
receiver_email =  os.getenv("RECIEVER_EMAIL") # Ganti dengan alamat email penerima

def send_email():
    # Membuat data email
    subject = "Contoh Broadcast Email"
    body = "Ini adalah contoh pesan broadcast email yang dikirim secara otomatis dengan Mailgun."
    data = {
        "from": sender_email,
        "to": receiver_email,
        "subject": subject,
        "text": body
    }

    # Mengirim email melalui API Mailgun
    try:
        response = requests.post(
            f"https://api.mailgun.net/v3/{mailgun_domain}/messages",
            auth=("api", mailgun_api_key),
            data=data
        )

        if response.status_code == 200:
            print("Email berhasil dikirim!")
        else:
            print(f"Terjadi kesalahan: {response.text}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Menjadwalkan pengiriman email setiap 1 menit
schedule.every(1).minutes.do(send_email)

# Looping untuk menjalankan tugas yang dijadwalkan
while True:
    schedule.run_pending()
    time.sleep(1)
