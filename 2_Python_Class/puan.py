class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif


class Soru:
    def netSayisi(self):
        self.net = self.dogruSayisi - self.yanlisSayisi / 4

    def hesapla(self):
        puan = 2 * self.net
        self.puan = puan


ogrenciAdi, ogrenciSoyadi, ogrenciSinif = "doruk", "kaya", "1a"
o1 = Ogrenci(ogrenciAdi, ogrenciSoyadi, ogrenciSinif)

print('doğru sayısı?')
dogruSayisi = input()
print('yanlış sayısı')
yanlisSayisi = input()

s1 = Soru()
s1.dogruSayisi = int(dogruSayisi)
s1.yanlisSayisi = int(yanlisSayisi)
s1.netSayisi()
s1.hesapla()

print(o1.ogrenciSinif + " sınıfından " + o1.ogrenciAdi + " " + o1.ogrenciSoyadi + ", sınavdan " + str(
    s1.puan) + " puan aldı")
