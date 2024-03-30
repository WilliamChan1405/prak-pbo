# a = 5
# b = 10

# for i in range(a,b):
#     print(i, end=' ')

# print()

# nama = ["anak1","anak2","anak3"]

# for anak in nama:
#     print(anak, end=' ')

# nama1 = ("anak1","anak2","anak3")

# print()

# for anak in nama1:
#     print(anak, end=' ')

# class Hewan:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia

#     def makan(self):
#         print(self.nama, " sedang makan...")

#     def berjalan(self):
#         print(f"{self.nama} sedang berjalan...")
    
#     def bersuara(self):
#         pass

# class Kucing(Hewan):
#     def __init__(self, nama, usia):
#         super().__init__(nama, usia)

#     # polymorphism inheritance
#     def bersuara(self):
#         print("miaw")
    
#     # polymorphism antar kelas
#     def tidur(self):
#         print("sedang tidur di kasur")

# class Anjing(Hewan):
#     def __init__(self, nama, usia):
#         super().__init__(nama, usia)

#     # polymorphism inheritance
#     def bersuara(self):
#         print("guk guk")

#     # polymorphism antar kelas
#     def tidur(self):
#         print("sedang tidur di kamar mandi")

# anggora = Kucing("anggora", 5)
# anggora.makan()
# anggora.berjalan()
# anggora.bersuara()
# anggora.tidur()

# anjing = Anjing("anjing",10)
# anjing.makan()
# anjing.berjalan()
# anjing.bersuara()
# anjing.tidur()

# import random

# class Manusia:
#     def __init__(self, nama: str, umur: int, tinggi_badan: float, berat_badan: float):
#         self.__nama = nama
#         self.__umur = umur
#         self.__tinggi_badan = tinggi_badan
#         self.__berat_badan = berat_badan

#     @staticmethod
#     def is_mature(umur):
#         if umur > 18:
#             print("Udah dewasa")
#         else:
#             print("Belum dewasa")

#     @classmethod
#     def generate(cls, nama):
#         return cls(nama, random.randrange(1,100), random.uniform(1,100),random.uniform(1,100))
    
#     # getter
#     @property
#     def nama(self):
#         return self.__nama

#     # getter
#     def get_nama(self):
#         return self.__nama

#     def get_umur(self):
#         return self.__umur

#     # setter
#     def set_umur(self, umur_baru):
#         self.__umur = umur_baru

#     umur = property(get_umur, set_umur)

#     def __str__(self) -> str:
#         return "Nama: {}\n" \
#             "Umur: {}\n" \
#             "TB: {}\n" \
#             "BB:{}".format(self.nama, self.umur, self.tinggi_badan, self.berat_badan) 

# class Hewan:
#     def __init__(self, nama: str, jenis: str):
#         self.nama = nama
#         self.jenis = jenis

#     def berjalan(self, orang: Manusia):
#         print(f"Hewan {self.nama} sedang berjalan")
#         # orang.nama = self.nama
#         # orang.set_umur(100)
#         orang.umur = 100

# orang = Manusia("seekor orang", 5, 2, 1)
# musang = Hewan("Akhdan", "Mamalia")

# print(orang.nama)
# print(orang.get_umur())

# musang.berjalan(orang)

# print(orang.get_nama())
# print(orang.get_umur())

# akhdan = Manusia.generate("akhdan")
# print(akhdan.umur)

# Manusia.is_mature(akhdan.umur)