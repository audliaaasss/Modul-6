# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:25:11 2022

@author: Audi Aulia
"""

print ("Program ini akan menentukan jumlah hari dalam bulan tertentu.")

F = False

year = ''

def Kabisat(year):
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        print ("29 hari dalam sebulan")
    else:
        print ("28 hari dalam sebulan")
        
def nonKabisat(month):
    if month in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        if month in [4, 6, 9, 11]:
            print ("30 hari dalam sebulan")
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            print ("31 hari dalam sebulan")
        elif month == 2:
            year = int(input("Masukkan tahun (e.g., 2022) : "))
            Kabisat(year) 
    else:
        print ("Error.")
        
while (not F):
    print("Masukkan 0 untuk menghentikan program")
    month = int(input("Masukkan bulan (1 - 12) : "))
    if month == 0:
        F = True
    else:
        nonKabisat(month)
        
print ("Terimakasih sudah menggunakan program ini, sampai berjumpa lagi.")