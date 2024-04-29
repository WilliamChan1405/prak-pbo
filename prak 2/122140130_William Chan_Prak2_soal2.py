import random

class Emas:

  def __init__(self, jenis_transaksi):
    self.__jenis_transaksi = jenis_transaksi
    self.__harga_emas = {
      "Ekspor": {
        "Indonesia": 750000,
        "Singapura": 780000,
        "Amerika Serikat": 820000,
      },
      "Impor": {
        "Australia": 720000,
        "Ghana": 700000,
        "India": 730000,
      },
    }
    self.__ongkos_kirim = {
      "Ekspor": {
        "Indonesia": 10000,
        "Singapura": 20000,
        "Amerika Serikat": 30000,
      },
      "Impor": {
        "Australia": 15000,
        "Ghana": 12000,
        "India": 18000,
      },
    }
    self.__pajak = {
      "Ekspor": 0.02,
      "Impor": 0.01,
    }

  def __del__(self):
    print(f"Terima kasih telah menggunakan sistem penjualan ekspor impor emas!")

  def start(self):
    negara = input("Masukkan negara tujuan Ekspor (Indonesia, Singapura, Amerika Serikat) atau asal Impor(Australia, Ghana, India): ")
    if negara not in self.__harga_emas[self.__jenis_transaksi]:
      print(f"Negara {negara} tidak tersedia untuk {self.__jenis_transaksi} emas.")
      return
    
    kuantitas = float(input("Masukkan kuantitas emas (gram): "))
    
    harga_emas = self.__harga_emas[self.__jenis_transaksi][negara]
    ongkos_kirim = self.__ongkos_kirim[self.__jenis_transaksi][negara]
    pajak = self.__pajak[self.__jenis_transaksi]
    
    total_biaya = (kuantitas * harga_emas) + ongkos_kirim
    if self.__jenis_transaksi == "Ekspor":
      total_biaya *= (1 - pajak)
    else:
      total_biaya *= (1 + pajak)
    
    print(f"Harga emas per gram: {harga_emas}")
    print(f"Ongkos kirim: {ongkos_kirim}")
    if self.__jenis_transaksi == "Ekspor":
      print(f"Pajak ekspor: {pajak * 100}%")
    else:
      print(f"Pajak impor: {pajak * 100}%")
    print(f"Total biaya {self.__jenis_transaksi} emas: {total_biaya}")


transaksi_ekspor = Emas("Ekspor")
transaksi_ekspor.start()

transaksi_impor = Emas("Impor")
transaksi_impor.start()