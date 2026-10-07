class Produk:
    def __init__(self, nama_barang, harga):
        self.nama_barang = nama_barang
        self.harga = harga

    def tampilkan_info(self):
        print(f'Nama Barang : {self.nama_barang}')
        print(f'Harga       : Rp{self.harga}')

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total_pembelian):
        if total_pembelian > 5000:
            return total_pembelian * 0.05
        else:
            return 0