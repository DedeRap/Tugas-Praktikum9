print ("===== File Handling =====")

def MakeFile(t):
    
    nama   = input("Masukkan Nama Anda : ")
    umur   = input("Masukkan Umur Anda : ")
    alamat = input("Masukkan Alamat Anda : ")
    email  = input("Masukkan Email Anda : ")
    dosen  = input("Masukkan Dosen Wali Anda : ")
    
    file = open("Biodata.txt", "w")
    file.write("Nama         : " + nama + "\nUmur         : " + umur + " tahun" + "\nAlamat       : " + alamat + "\nEmail        : " + email + "\nDosen Wali   : " + dosen )
    file.close()
    
#Batas=======================================================================
    
def ReadFile(b):
    
    print("\nData Anda    :")
    file = open("Biodata.txt", "r+")
    text = file.read()
    print(text)
    file.close()
    
z = True
while(z == True):
    
    print("\nTekan 1 untuk membuat file atau tekan 2 untuk membaca file atau tekan 0 untuk keluar :")
    n = int(input("Masukkan menu angka : "))
    if (n == 1):
        MakeFile(n)
    elif (n == 2):
        ReadFile(n)
    else :
        z = False