class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif


class Soru:
    def netSayisi(self, dogruSayisi, yanlisSayisi):
        self.net = dogruSayisi - yanlisSayisi / 4

    def hesapla(self):
        puan = 2 * self.net
        self.puan = puan


ogrenciAdi, ogrenciSoyadi, ogrenciSinif = "doruk", "kaya", "1a"
o1 = Ogrenci(ogrenciAdi, ogrenciSoyadi, ogrenciSinif)


dogruSayisi = int(input('doğru sayısı?'))
yanlisSayisi = int(input('yanlış sayısı?'))

s1 = Soru()
s1.netSayisi(dogruSayisi, yanlisSayisi)
s1.hesapla()

print(o1.ogrenciSinif + " sınıfından " + o1.ogrenciAdi + " " + o1.ogrenciSoyadi + ", sınavdan " + str(
    s1.puan) + " puan aldı")
