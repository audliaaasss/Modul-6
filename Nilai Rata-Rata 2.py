# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:03:59 2022

@author: Audi Aulia
"""
def rata_rata(data = [], total = 0):
    n = int(input('Jumlah nilai : '))
    for i in range(0,n):
        isi = str(input('Masukkan Nilaimu : '))
        if isi == 'A':
            data.append(isi)
            total += 4.00
            print('Nilai = 4')
        elif isi == 'A-':
            data.append(isi)
            total += 3.75
            print('Nilai = 3.75')
        elif isi == 'B+':
            data.append(isi)
            total += 3.50
            print('Nilai = 3.50')
        elif isi == 'B':
            data.append(isi)
            total += 3.00
            print('Nilai = 3')
        elif isi == 'B-':
            data.append(isi)
            total += 2.75
            print('Nilai = 2.75')
        elif isi == 'C+':
            data.append(isi)
            total += 2.50
            print('Nilai = 2.5')
        elif isi == 'C':
            data.append(isi)
            total += 2.00
            print('Nilai = 2')
        elif isi == 'C-':
            data.append(isi)
            total += 1.75
            print('Nilai = 1.75')
        elif isi == 'D':
            data.append(isi)
            total += 1.50
            print('Nilai = 1.5')
        elif isi == 'E':
            data.append(isi)
            total += 1.25
            print('Nilai = 1.25')
        
        mean = total/n
    print("\n Rata-rata nilaimu adalah %0.2f" % mean)
 
rerata = rata_rata()
print(rerata)