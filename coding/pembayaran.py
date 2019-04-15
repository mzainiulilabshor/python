
from texttable import Texttable


 
def pembayaran () :
        
        biaya_bulanan=0
        biaya_uts=0
        biaya_uas=0
        nim      =[]
        print ("\t------PROGRAM PEMBAYARAN -------")
       
        
        nama  =  input (" Nama  :")
        nim   =  input (" Nim   :")
        kelas =  input (" Kelas :")
        


        table = Texttable (max_width=400)
        table.add_rows([["No","Jenis Pembayaran"],["1.)"," Pembayaran Bulanan "],["2.)"," Pembayaran UTS "],["3.)"," Pembayaran UAS "],["4.)"," Exit"]])
                                                                                                                     
        print(table.draw())
        jawab="y"
        while(jawab=="y"):
            
                pilih = input (" Masukan pilihan anda : ")
              
                if (pilih=="1"):
                        print("\n\t( =>=> Pembayaran Bulanan <=<= ) \n")
                        jumlah_bulan = int( input (" Berapa bulan yang ingin anda bayar? "))
                        biaya_bulanan=jumlah_bulan*500000
                        jawab = input (" ingin tambah Pembayaran (y/t) : ")
                if (pilih=="2"):
                        print("\n\t( =>=> Pembayaran UTS <=<= ) \n")
                        uts = int(input (" Berapa mata kuliah yang ingin anda bayar ? : "))
                        biaya_uts=uts*50000
                        jawab = input (" ingin tambah Pembayaran (y/t) : ")                               
                if (pilih=="3"):
                        print("\n\t( =>=> Pembayaran UAS <=<= ) \n")
                        uas =int( input (" Berapa mata kuliah yang ingin anda bayar ? : "))
                        biaya_uas=uas*50000
                        jawab = input (" ingin tambah pembayaran (y/t) : ")
                if (pilih=="4"):
                        break
       
                
        biaya_admin  = 5000
        biaya_seminar= 100000
        biaya_kas    = 20000        
        biaya_total  = biaya_bulanan+biaya_uts+biaya_uas+biaya_admin+biaya_seminar+biaya_kas
        table = Texttable (max_width=700)
        table.set_cols_dtype(["t","t","a","a","a","a","a","a","a","a"])
        table.add_rows([["nama","nim","kelas","Bulanan","UTS","UAS","Admin","Seminar","Kas","Total"],
                        [nama,nim,kelas,biaya_bulanan,biaya_uts,biaya_uas,biaya_admin,biaya_seminar,biaya_kas,biaya_total]])
        print(table.draw())

        
       


               
