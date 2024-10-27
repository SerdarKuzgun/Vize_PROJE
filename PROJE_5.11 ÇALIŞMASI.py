class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def bilgileri_goster(self):
        return f"Ad: {self.ad}, Yaş: {self.yas}"

class Ogrenci(Kisi):
    def __init__(self, ad, yas, ogrenci_numarasi):
        super().__init__(ad, yas)
        self.ogrenci_numarasi = ogrenci_numarasi

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Öğrenci Numarası: {self.ogrenci_numarasi}"

class Ogretmen(Kisi):
    def __init__(self, ad, yas, ders):
        super().__init__(ad, yas)
        self.ders = ders

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Ders: {self.ders}"

# Örnek Kullanım
ogrenci = Ogrenci("Ali", 20, "S12345")
ogretmen = Ogretmen("Ayşe", 30, "Matematik")

print(ogrenci.bilgileri_goster())
print(ogretmen.bilgileri_goster())
