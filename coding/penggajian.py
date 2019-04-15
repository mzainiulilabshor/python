def Gajih():
    from texttable import Texttable
    table = Texttable ()
    jawab = "y"
    no = 0
    nama = []
    jabatan = []
    gaji = []
    while (jawab == "y"):
        nama.append(input("\n Masukan Nama :"))
        print ( " \n\t => supervisor \n\t => leader \n\t => operator ")
        jab = input("jabatan :")
        jabatan.append(jab)                                                                                 

        if (jab == 'supervisor'):
            gaji.append('Rp 7.000.000,00')
            jawab = input("\n Tambahan data(y/t) :")
            no +=1

        elif(jab == 'leader'):
            gaji.append('Rp 6.000.000,00')
            jawab = input("\n Tambahan Data(y/t) :")
            no +=1
        elif (jab == 'operator'):
            gaji.append('Rp 4.300.000,00' )
            jawab = input("\n Tambahan Data(y/t) :")
            no +=1
        else :
            print ("\n Jabatan yang anda masukan tidak tersedia \n")
            break

                     
    for i in range (no) :
        table.add_rows([['No' ,'Nama','Jabatan','Gaji'],
                        [i+1, nama[i],jabatan[i],gaji[i]]])

    print(table.draw())

    print ( " \n\n\tArigatou Ghozaimash ")
