print('='*47)
print('='*15, 'REAL MAGHRIB FC', '='*15)
print('='*47)

#uname
bisa = ['cakjidan', 'raulgonjales', 'karimbenjema']
n = input(str("Masukkan username anda: "))
user = n.lower()
player=[]
#pilihan
while True : 
    if user in bisa:
        print('='*5, "Selamat Datang",  n ,"="*5)
        print('1. Tambah Data Pemain')
        print('2. Hapus Data Pemain')
        print('3. Tampilkan Data Pemain')
        print('4. Exit')
        p =input('Masukkan pilihan anda: ')
    if p =="1":
        ta = input('Tambahkan data pemain: ')
        player.append(ta)
        print('Data', "'",ta,"'","Berhasil ditambahkan")
    elif p == "2":
        h = input("Masukkan Data pemain yang akan dihapus: ")
        if h not in player:
            print("Data","'",h,"'","tidak ditemukan")
        else: 
            player.remove(h)
            print("Data")
    elif p == "3": 
        print('Affiliasi Kerajaan Utara : ')
    else : 
        print('Adios ....', n, 'GLHF')






