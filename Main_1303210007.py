# nomor 1

# buka dan baca berkas teks, split berdasarkan
# line baru
data_catur = open('catur.txt')
data_catur = data_catur.read().splitlines()

# buat dictionary daftar poin berdasarkan file teks, key berisi nama pemain dan value berupa total poin yang diperoleh
# deklarasi dict
daftar_poin = {}

# for loop untuk proses data
for i in data_catur:
    # split variable iterasi berdasarkan spasi
    nama = i.split(' ')
    # nama[0] adalah permain putih, dan nama[-1] akan di split lagi berdasarkan string '-'
    # lalu dievaluasi tipenya menggunakan eval() agar menjadi float. apabila nama sudah
    # ada di dict sebagai key maka update skornya, jika belum maka masukkan nama tsb
    # sebagai key baru dengan index pertama hasil split sebagai poinnya
    if nama[0] in daftar_poin:
        daftar_poin.update({nama[0]: daftar_poin[nama[0]] + eval(nama[-1].split('-')[0])})
    else:
        daftar_poin.update({nama[0]: eval(nama[-1].split('-')[0])})
    # sama halnya seperti di atas tapi untuk pemain hitam
    if nama[1] in daftar_poin:
        daftar_poin.update({nama[1]: daftar_poin[nama[1]] + eval(nama[-1].split('-')[1])})
    else:
        daftar_poin.update({nama[1]: eval(nama[-1].split('-')[1])})

# daftar fungsi
# fungsi pemain yg digunakan utk return bnyknya pemain yg bertanding
def pemain(daftar_pemain: dict):
    # return daftar pemain lagi untuk diproses lebih lanjut
    # pada main program, dan return jumlah pemain menggunakan len()
    return daftar_pemain, len(daftar_pemain)


# fungsi juara yg digunakan utk  menampilkan pemain dgn poin tertinggi
def juara(daftar_pemain: dict, action: int):
    # list utk menyimpan pemenang jika ada yang poinnya sama dan
    # mereka yang merupakan pemilik poin paling tinggi
    kandidat_pemenang = []

    # cari poin tertinggi bila action = 1
    if action == 1:
        poin_diminta = max(daftar_pemain.values())
    # sebaliknya cari poin terendah bila action = 2
    else:
        poin_diminta = min(daftar_pemain.values())

    # for loop untuk mengecek setiap pemain dan poin mereka. bila
    # poin sama dengan variable poin_tertinggi maka append ke list
    for personnel in daftar_pemain.items():
        if personnel[-1] == poin_diminta:
            kandidat_pemenang.append(personnel)

    # return list
    return kandidat_pemenang

# main program yg digunakan utk menampilkan dictionary dan memanggil fungsi yg dibuat
# main program
print(daftar_poin)  # print dict

# karena return value fungsi pemain() berupa tuple maka 
# bisa langsung diassign pada 2 variable 
players, jumlah = pemain(daftar_poin)

# minta user untuk input apa yang ingin dilihat (pemain dengan
# poin tertinggi atau terendah) lalu panggil fungsi juara()
while True:
    try:
        pilihan = int(input("\nInput nomor berdasarkan apa yang Anda ingin lihat:"
                            "\n1. Pemain dengan total poin tertinggi"
                            "\n2. Pemain dengan total poin terendah"
                            "\nInput Anda = "))
        # bila pemain memasukkan angka selain 1 atau 2 maka ulangi lagi
        if pilihan not in (1, 2):
            print("\nMohon masukkan nomor sesuai yang tertera pada layar")
        else:
            winner = juara(daftar_poin, pilihan)
            break
    # bila user memasukkan selain angka maka print statement di bawah
    except ValueError:
        print("\nMohon masukkan angka, bukan yang lainnya")

# print hasil dari pemanggilan fungsi
print(f"\nJumlah total pemain yang bertanding adalah {jumlah} orang, dengan rincian pemain: ")
for i in players:
    print(i)
# pilihan 1 = poin tertinggi, pilihan 2 = poin terendah
if pilihan == 1:
    print(f"\nPoin tertinggi dalam pertandingan diraih oleh:")
    for j in winner:
        print(f"{j[0]} dengan poin total {j[1]}")
else:
    print(f"\nPoin terendah dalam pertandingan diraih oleh:")
    for j in winner:
        print(f"{j[0]} dengan poin total {j[1]}")
