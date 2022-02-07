class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, i):
        self.yetenekler.append(i)


k1 = Insan('doruk', 'kaya', '23', 'türkiye', 'istanbul')
k1.yetenek_ekle('python')
k1.yetenek_ekle('yüzme')
ad, soyad, yas, ulke, sehir, yetenekler = k1.kisi_bilgileri()
print(k1.kisi_bilgileri())
