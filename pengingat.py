import requests
import time
import datetime

TOKEN = "7336091968:AAFJ1rnjFJFjPb1hfBnzy7ZGcGVFB8LUijc"
CHAT_ID = "5127235287"

daily_ideas = [
    "Hari 1: Aplikasi menggambar di udara menggunakan hand tracking.",
    "Hari 2: Kontrol presentasi PowerPoint dengan gestur tangan.",
    "Hari 3: Game tebak gerakan tangan.",
    "Hari 4: Navigasi menu TV atau Smart Home pakai tangan.",
    "Hari 5: Kontrol volume atau musik pakai gestur jari.",
    "Hari 6: Sistem input virtual (keyboard di udara).",
    "Hari 7: Aplikasi senam/tari virtual yang baca gestur.",
    "Hari 8: Deteksi 'angkat tangan' untuk absen online.",
    "Hari 9: Game rhythm pakai tangan (kayak Guitar Hero tapi di udara).",
    "Hari 10: Kontrol robot mainan dengan gestur tangan.",
    "Hari 11: Pengendali kamera webcam (zoom, rotate) dengan tangan.",
    "Hari 12: Navigasi website cukup dengan tangan.",
    "Hari 13: Game 'batu-gunting-kertas' otomatis lawan AI.",
    "Hari 14: Gambar abstrak otomatis dari gerakan tangan.",
    "Hari 15: Kontrol slide PDF untuk belajar/jelasin materi.",
    "Hari 16: Game menangkis bola virtual pakai telapak tangan.",
    "Hari 17: Menulis huruf di udara dan dikenali sebagai teks.",
    "Hari 18: Puzzle game gestur (gerakan untuk buka kunci).",
    "Hari 19: Remote kendali video player (YouTube, Netflix).",
    "Hari 20: Alat bantu tunarungu/dengar menggunakan gerakan tangan.",
    "Hari 21: Aplikasi edukasi anak: belajar angka & huruf lewat tangan.",
    "Hari 22: Virtual paint pakai tangan dan tracking warna.",
    "Hari 23: Simulasi alat musik virtual (gitar/drum) dengan tangan.",
    "Hari 24: Aplikasi interaktif buat museum atau pameran.",
    "Hari 25: Kontrol smart mirror pakai tangan.",
    "Hari 26: Kaligrafi digital di udara.",
    "Hari 27: Uji refleks dan gerak dengan feedback waktu nyata.",
    "Hari 28: Filter kamera otomatis berdasarkan posisi tangan.",
    "Hari 29: Ubah ekspresi wajah karakter 3D pakai tangan.",
    "Hari 30: Buat sistem skor otomatis untuk olahraga (contoh: angkat tangan = goal)."
]


def kirim_ide_harian():
    hari = (datetime.datetime.now().day - 1) % len(daily_ideas)
    pesan = f"Ide Harianmu 🎯:\n{daily_ideas[hari]}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": pesan})

last_sent_date = None
while True:
    now = datetime.datetime.now()
    
    
    if now.hour == 19 and now.minute == 46 and last_sent_date != now.date():
        kirim_ide_harian()
        last_sent_date = now.date()  

    time.sleep(30)  