
import random

# === Kullanıcıdan gelen veri (örnek) ===
kullanici_mesaji = "Bugün kendimi huzursuz ve gergin hissediyorum."

# === GölgeZihin - Shadow AI'ın karakteri ===
def analiz_et(mesaj):
    if "huzursuz" in mesaj or "gergin" in mesaj:
        return "endise"
    elif "mutlu" in mesaj:
        return "pozitif"
    else:
        return "nötr"

# === Kullanıcı tarzı cevap (taklit) ===
def kullanici_tarzinda_cevap(mesaj):
    return f"Anlıyorum... Bazen böyle hissetmek normal. Belki biraz yürüyüş iyi gelir?"

# === Gölge tarzı cevap (bir adım ilerisi) ===
def golge_tarzinda_cevap(mesaj):
    duygudurum = analiz_et(mesaj)
    if duygudurum == "endise":
        return "Gerginliğini fark ettim. Belki nefes egzersizi yapmayı denemelisin, istersen birlikte başlayalım."
    elif duygudurum == "pozitif":
        return "Bu güzel! Bu ruh halini nasıl sürdürebileceğini birlikte keşfedelim."
    else:
        return "Nötr bir ruh halindesin. Hedeflerini hatırlamak ister misin?"

# === Gölgeyle Yarış Modu ===
def golgeyle_yaris():
    print("[Kullanıcı Cevabı]")
    print(kullanici_tarzinda_cevap(kullanici_mesaji))
    print("\n[Gölge AI Cevabı]")
    print(golge_tarzinda_cevap(kullanici_mesaji))

if __name__ == "__main__":
    print("=== TILKIVERSE AI DEMO v0.1 ===")
    print(f"Girdi: {kullanici_mesaji}")
    print("-------------------------------")
    golgeyle_yaris()
