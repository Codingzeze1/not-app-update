import json
import os
import urllib.request
from datetime import datetime

__version__ = "1.1.0"

NOTLAR_DOSYASI = "notlar.json"

def notlari_yukle():
    if not os.path.exists(NOTLAR_DOSYASI):
        return []
    with open(NOTLAR_DOSYASI, "r", encoding="utf-8") as f:
        return json.load(f)

def notlari_kaydet(notlar):
    with open(NOTLAR_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(notlar, f, ensure_ascii=False, indent=4)

def not_ekle():
    metin = input("Not: ")
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notlar = notlari_yukle()
    notlar.append({"metin": metin, "tarih": zaman})
    notlari_kaydet(notlar)
    versiyonu_arttir()
    print("✅ Not kaydedildi.")

def notlari_listele():
    notlar = notlari_yukle()
    if not notlar:
        print("📝 Hiç not yok.")
    for i, notum in enumerate(notlar, 1):
        print(f"{i}. [{notum['tarih']}] {notum['metin']}")

def versiyonu_goster():
    try:
        with open("version.txt", "r") as dosya:
            version = dosya.read().strip()
            print(f"📦 Uygulama Sürümü: {version}")
    except FileNotFoundError:
        print("❌ version.txt dosyası bulunamadı.")
def versiyonu_arttir():
    try:
        with open("version.txt", "r") as dosya:
            version = dosya.read().strip()
        
        major, minor, patch = version.split(".")
        patch = str(int(patch) + 1)  # patch bir arttırılır

        yeni_version = f"{major}.{minor}.{patch}"

        with open("version.txt", "w") as dosya:
            dosya.write(yeni_version)
        print(f"🔁 Yeni sürüm: {yeni_version}")

    except Exception as e:
        print(f"❌ Versiyon güncellenemedi: {e}")
        
def guncel_surum_kontrol_et():
    try:
        # GitHub'daki güncel sürüm dosyasının RAW bağlantısı
        url = "https://raw.githubusercontent.com/Codingzeze1/not-app-update/refs/heads/main/latest_version.txt"
        response = urllib.request.urlopen(url)
        guncel_version = response.read().decode("utf-8").strip()

        with open("version.txt", "r") as dosya:
            mevcut_version = dosya.read().strip()

        if guncel_version != mevcut_version:
            print(f"⬆️ Yeni sürüm mevcut: {mevcut_version} → {guncel_version}")
            print("📥 Lütfen yeni sürümü indirip güncelleyin.")
        else:
            print("✅ En güncel sürümü kullanıyorsunuz.")
    except Exception as e:
        print(f"❌ Güncelleme kontrolü başarısız: {e}")


def main():
    while True:
        print("\n🔸 Komutlar: ekle, listele, version, cikis")
        komut = input("Komut: ").strip().lower()

        if komut == "ekle":
            not_ekle()
        elif komut == "listele":
            notlari_listele()
        elif komut == "version":
            print(f"📌 Sürüm: {__version__}")
        elif komut == "guncelleme":
            guncel_surum_kontrol_et()

        elif komut == "cikis":
            print("Çıkılıyor...")
            break
        else:
            print("❗ Geçersiz komut.")

if __name__ == "__main__":
    main()


#Lokal sürüm yönetimi yapıyor ✅
#Otomatik patch güncellemesi yapıyor ✅
#Online olarak en güncel sürümü kontrol edebiliyor ✅
