from coding.penggajian import Gajih
from coding.penilaian  import Nilai
from coding.pembayaran import pembayaran
from coding.kalkulator import kalkulator
def Login ():
    import getpass
    print ("\t Login Akun \n")
    user = input(" Username: ")
    password = getpass.getpass (" Password: ")
    if user == 'ulil' and password == '1122':
         pilihan ()
    else:
         print ("\n Password yang anda masukan Salah")
         Login ()
def pilihan () :
    print("----PILIH MENU----")
    print("\n\t----pilihan----\n\t1. Gajih\n\t2. Nilai\n\t3. Pembayaran\n\t4. kalkulator")
    pilih = input("\nsilahkan pilih : ")
    if pilih == "1" :
        Gajih ()
        lagi ()
    elif pilih == "2" :
        Nilai ()
        lagi ()
    elif pilih == "3" :
        pembayaran ()
        lagi ()
    elif pilih == "4" :
        kalkulator ()
        lagi ()
    else :
        exit
        print ("\n\t-----terima kasih----")
def lagi ():
    tanya = input("\nkembali ke menu pilihan (y/t)? ")
    if tanya == "y":
        pilihan ()
    else :
        print ("\n\t-----terima kasih----")
        input("")
        exit        
Login()
