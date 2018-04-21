import texttable as tt
import getpass
from perhitungan.calculator import cal
from perhitungan.pembayaran import pembayaran
from perhitungan.penilaian import nilai_mahasiswa


def menu():
    print("=============================================")
    print("\n\t---pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. kalkulator")

    pilih = input("\n\tsilakan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2" :
        pembayaran()
    elif pilih == "3" :
        cal()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y\t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tsalah input...........!!!")

username = input("\nUsername : ")
password = getpass.getpass()
print("============================================")

if username == "april" and password == "iniapril":
    menu()

else:
    print ("maaf password atau username mu salah..............!!!")
                
