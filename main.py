from coba import Produk

jumlah_produk = int(input('Masukan jumlah produk : '))

total_seluruh = 0

for i in range(jumlah_produk):
    print(f'\nProduk ke-{i + 1}')

    nama_produk = input('Masukan nama produk: ')
    harga_produk = float(input('Masukan harga produk: '))
    jumlah_beli = int(input('Masukan jumlah beli: '))

    produk = Produk(nama_produk, harga_produk)

    produk.tampilkan_info()

    total_produk = produk.hitung_total(jumlah_beli)

    print(f'Total pembelian : Rp{total_produk}')

    total_seluruh = total_seluruh + total_produk

diskon = produk.hitung_diskon(total_seluruh)

total_bayar = total_seluruh - diskon


print(f'Total Pembelian : Rp{total_seluruh}')
print(f'Diskon 5%       : Rp{diskon}')
print(f'Total Bayar     : Rp{total_bayar}')