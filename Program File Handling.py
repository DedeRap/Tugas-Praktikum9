print("===== Program File Handling =====")


def membuat():
    a = input("Masukkan Nama File           : ")
    b = input("Masukkan Nama Anda           : ")
    c = input("Masukkan NIM Anda            : ")
    d = input("Masukkan Tahun Angkatan Anda : ")
    
    file = open(a + ".txt","w")
    file.write("\nNama : " + b + "\nNIM : " + c + "\nTahun Angkatan : " + d)
    file.close()
    
def membaca():
    a = input("Masukkan Nama File yang Telah Anda Buat(Tambahkan .txt Dibelakang) : ")
    print("\nIsi Data Anda : ")
    file = open(a, "r+")
    text = file.read()
    print(text)
    file.close()
    
def menambah():
    a = input("Masukkan Nama File yang Telah Anda Buat(Tambahkan .txt Dibelakang) : ")
    file = open(a, "a")
    r = input("Masukkan Data yang Ingin Ditambah : ")
    t = input("Masukkan Isi Data Tersebut        : ")
    file.write("\n" + r + " : " + t)
    file.close()     
        
#Batas=================================================================================

z = True
while (z == True):
    print("\nSilahkan Pilih Menu File Berikut :")
    print("1. Membuat dan Menulis File.")
    print("2. Membaca File.")
    print("3. Menambahkan Text Pada File.")
    print("4. Keluar dari Program.")
    
    l = int(input("\nMasukkan Pilihan Berupa Angka (1/2/3/4) : "))
    
    if (l == 1):
        membuat()
    elif (l == 2):
        membaca()
    elif (l == 3):
        menambah()
    else :
        z = False
        
print("\nTerima Kasih, Anda Telah Menggunakan Program Saya")  