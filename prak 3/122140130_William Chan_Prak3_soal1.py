# class MAHASEWA:
#     global_variable_jumlah = 0

#     def __init__(self,nama,semester):
#         self.nama = nama
#         self.semester = semester
#         MAHASEWA.global_variable_jumlah = MAHASEWA.global_variable_jumlah + 1

#     def printjumlah(self):
#             print ("Total Mahasewa adalah ", MAHASEWA.global_variable_jumlah, "orang")

#     def printprofile(self):
#             print ("Nama : " , self.nama)
#             print ("semester : ", self.semester)
            
# mhs1 = MAHASEWA("Andi", 1)
# mhs2 = MAHASEWA("Budi", 2)

# mhs1.printprofile()
# mhs1.printjumlah()
# mhs2.printprofile()
# mhs2.printjumlah()

# class MUBIL:
#     _merk = None
#     _warna = None

#     def __init__(self,warna,merk):
#         self._merk = merk
#         self._warna = warna

#     def _TampilMobil(self):
#         print ("MEREK MOBIL = ", self._merk)
#         print ("WARNA MOBIL = ", self._warna)

# mobil1 = MUBIL("merah", "BMW")
# mobil1._TampilMobil()

# class Mobil:
#     __bensin = 0  # Liter
#     __odometer = 0  # Kilometer

#     def __init__(self):
#         pass

#     def __isi_bensin(self, liter):
#         self.__bensin += liter
#         if self.__bensin > 60:
#             self.__bensin = 60

#     def __mengendarai(self, kilometer):
#         if kilometer > self.__bensin:
#             kilometer = self.__bensin
#         self.__bensin -= kilometer
#         self.__odometer += kilometer

#     def lihat_info(self):
#         print(f"Bensin: {self.__bensin} liter")
#         print(f"Odometer: {self.__odometer} kilometer")


# mobil = Mobil()
# mobil.lihat_info()
# mobil.__isi_bensin()
# mobil.lihat_info()
# mobil.__mengendarai(20)
# mobil.lihat_info()
# mobil.__mengendarai(50)
# mobil.lihat_info()
# mobil.__mengendarai(10)
# mobil.lihat_info()
# mobil.__isi_bensin()
# mobil.__isi_bensin()
# mobil.lihat_info()

class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for i, barang in enumerate(Dagangan.list_barang):
            if barang[0] == self.__nama:
                del Dagangan.list_barang[i]
                print(f"{self.__nama} dihapus dari toko!")
                break

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah")
        for i, barang in enumerate(cls.list_barang):
            print(f"{i+1}. {barang[0]} seharga Rp {barang[2]} (stok: {barang[1]})")


Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

del Dagangan1
Dagangan.lihat_barang()