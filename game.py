import time
import random
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Takımlar ve sürücüler
takimlar = {
    "Mercedes-AMG PETRONAS": {
        "pilots": [
            {"isim": "Lewis Hamilton", "hız": 9, "dayaniklilik": 9, "yas": 38, "tecrube": 18, "tur_hizi": 1.4},
            {"isim": "George Russell", "hız": 8, "dayaniklilik": 9, "yas": 25, "tecrube": 5, "tur_hizi": 1.3}
        ]
    },
    "Red Bull Racing": {
        "pilots": [
            {"isim": "Max Verstappen", "hız": 10, "dayaniklilik": 9, "yas": 26, "tecrube": 7, "tur_hizi": 1.5},
            {"isim": "Sergio Pérez", "hız": 8, "dayaniklilik": 9, "yas": 34, "tecrube": 12, "tur_hizi": 1.3}
        ]
    },
    "Ferrari": {
        "pilots": [
            {"isim": "Charles Leclerc", "hız": 9, "dayaniklilik": 7, "yas": 27, "tecrube": 6, "tur_hizi": 1.35},
            {"isim": "Carlos Sainz Jr.", "hız": 8, "dayaniklilik": 8, "yas": 29, "tecrube": 8, "tur_hizi": 1.3}
        ]
    },
    "McLaren": {
        "pilots": [
            {"isim": "Lando Norris", "hız": 9, "dayaniklilik": 7, "yas": 24, "tecrube": 5, "tur_hizi": 1.3},
            {"isim": "Oscar Piastri", "hız": 9, "dayaniklilik": 8, "yas": 22, "tecrube": 2, "tur_hizi": 1.25}
        ]
    },
    "Aston Martin Aramco": {
        "pilots": [
            {"isim": "Fernando Alonso", "hız": 8, "dayaniklilik": 9, "yas": 42, "tecrube": 20, "tur_hizi": 1.4},
            {"isim": "Lance Stroll", "hız": 7, "dayaniklilik": 8, "yas": 25, "tecrube": 6, "tur_hizi": 1.25}
        ]
    },
    "Alpine": {
        "pilots": [
            {"isim": "Esteban Ocon", "hız": 8, "dayaniklilik": 8, "yas": 27, "tecrube": 6, "tur_hizi": 1.35},
            {"isim": "Pierre Gasly", "hız": 8, "dayaniklilik": 7, "yas": 28, "tecrube": 7, "tur_hizi": 1.3}
        ]
    },
    "Haas": {
        "pilots": [
            {"isim": "Kevin Magnussen", "hız": 7, "dayaniklilik": 8, "yas": 31, "tecrube": 9, "tur_hizi": 1.2},
            {"isim": "Nico Hülkenberg", "hız": 7, "dayaniklilik": 8, "yas": 36, "tecrube": 12, "tur_hizi": 1.25}
        ]
    },
    "Williams": {
        "pilots": [
            {"isim": "Alexander Albon", "hız": 7, "dayaniklilik": 8, "yas": 27, "tecrube": 5, "tur_hizi": 1.3},
            {"isim": "Logan Sargeant", "hız": 6, "dayaniklilik": 7, "yas": 22, "tecrube": 1, "tur_hizi": 1.2}
        ]
    },
    "Racing Bulls": {
        "pilots": [
            {"isim": "Yuki Tsunoda", "hız": 7, "dayaniklilik": 8, "yas": 23, "tecrube": 3, "tur_hizi": 1.2},
            {"isim": "Daniel Ricciardo", "hız": 8, "dayaniklilik": 7, "yas": 34, "tecrube": 15, "tur_hizi": 1.25}
        ]
    },
    "Kick Sauber": {
        "pilots": [
            {"isim": "Valtteri Bottas", "hız": 8, "dayaniklilik": 9, "yas": 35, "tecrube": 10, "tur_hizi": 1.3},
            {"isim": "Zhou Guanyu", "hız": 7, "dayaniklilik": 8, "yas": 24, "tecrube": 2, "tur_hizi": 1.2}
        ]
    }
}

# Pist listesi ve bilgileri
yaris_pistleri = [
    {"adi": "Monza", "uzunluk": 5.793, "tur_sayisi": 10},
    {"adi": "Silverstone", "uzunluk": 5.891, "tur_sayisi": 8},
    {"adi": "Suzuka", "uzunluk": 5.807, "tur_sayisi": 9},
    {"adi": "Spa-Francorchamps", "uzunluk": 7.004, "tur_sayisi": 7},
    {"adi": "Monaco", "uzunluk": 3.337, "tur_sayisi": 15},
    {"adi": "Interlagos", "uzunluk": 4.309, "tur_sayisi": 12},
    {"adi": "Marina Bay", "uzunluk": 5.063, "tur_sayisi": 11},
    {"adi": "Austin", "uzunluk": 5.513, "tur_sayisi": 9},
    {"adi": "Montreal", "uzunluk": 4.361, "tur_sayisi": 10},
    {"adi": "Yas Marina", "uzunluk": 5.554, "tur_sayisi": 9},
]

# Rastgele olaylar
rastgele_olaylar = [
    ("Küçük bir mekanik arıza yaşadı", 5),
    ("Çarpışma nedeniyle zaman kaybetti", 10),
    ("Pit stopta zaman kaybetti", 7),
    ("Lastik patlaması nedeniyle yavaşladı", 12),
    ("Motor sorunları yaşadı", 15),
    ("Sarı bayraklarda yavaşlamak zorunda kaldı", 3),
    ("Bir rakiple temas nedeniyle aracın aerodinamiği zarar gördü", 8),
    ("Araçta geçici bir elektronik arıza oluştu", 6),
    ("Vites kutusunda kısa süreli bir problem yaşandı", 4),
    ("Pit alanı ihlali nedeniyle ceza aldı", 10),
]

# F1 puanlama sistemi
puan_sistemi = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]  # 10 sıra

# Yarış simülasyonu fonksiyonu
def yaris_simulasyonu():
    sampiyona_sonuc = {"sürücü": {}, "takim": {}}
    
    for i in range(10):  # 10 yarışlık sezon simülasyonu
        print(f"\nYarış {i+1}")
        yaris_pisti = random.choice(yaris_pistleri)
        print(f"Pist: {yaris_pisti['adi']} ({yaris_pisti['uzunluk']} km) - Toplam Turlar: {yaris_pisti['tur_sayisi']}")
        
        # Her yarışta rastgele 3 olay seç
        for olay in random.sample(rastgele_olaylar, k=3):
            print(Fore.YELLOW + f"Olay: {olay[0]} - Zaman Kaybı: {olay[1]} saniye")

        # Yarış sonucu tahmini
        sinav_sonuclari = []
        for takim, bilgiler in takimlar.items():
            for surucu in bilgiler["pilots"]:
                tur_hizi = surucu["tur_hizi"] * random.uniform(0.9, 1.1)  # Rastgele faktör
                hiz = surucu["hız"] * random.uniform(0.95, 1.05)
                dayanıklılık = surucu["dayaniklilik"] - random.randint(0, 5)

                # Sürücüyü sıralama
                sinav_sonuclari.append({"isim": surucu["isim"], "hiz": hiz, "tur_hizi": tur_hizi, "takim": takim})

        # Sıralama yap
        sinav_sonuclari.sort(key=lambda x: x["hiz"], reverse=True)

        # Öne çıkan 3 sürücüyü altın renk ile göster
        for i, result in enumerate(sinav_sonuclari):
            if i == 0:
                renk = Fore.YELLOW  # Altın sarısı 1. pilot
            elif i == 1:
                renk = Fore.YELLOW  # 2. pilot
            elif i == 2:
                renk = Fore.YELLOW  # 3. pilot
            else:
                renk = Fore.WHITE  # Diğer pilotlar
            
            print(renk + f"{result['isim']} ({result['takim']}): {result['hiz']:.2f} km/h")
        
        # Şampiyonada yer alan sonuçlar
        for surucu in sinav_sonuclari:
            if surucu['isim'] not in sampiyona_sonuc["sürücü"]:
                sampiyona_sonuc["sürücü"][surucu['isim']] = 0
            rank = sinav_sonuclari.index(surucu)
            if rank < len(puan_sistemi):
                sampiyona_sonuc["sürücü"][surucu['isim']] += puan_sistemi[rank]

        print("\n=== Şampiyonaya Genel Bakış ===")
        print("\nSürücü Puan Durumu:")
        for isim, puan in sorted(sampiyona_sonuc["sürücü"].items(), key=lambda x: x[1], reverse=True):
            print(f"{isim}: {puan} Puan")

# Yarış başlatma
if __name__ == "__main__":
    yaris_simulasyonu()
