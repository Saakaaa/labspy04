list=["a", "b", "c", "d", "e"]

print("Tampilkan Elemen ke 3:",list[2])
print("Ambil Elemen ke 2 sampai ke 4:",list[1:4])
print("Ambil Elemen Terakhir:",list[-4])

#Merubah Elemen ke 4 dengan nilai lain
list[3] = "f"
print("Merubah elemen 4 dengan nilai lain:",list)

#Merubah Elemen Ke 4 Sampai Terakhir
list[3:] = "j","k"
print("Merubah elemen 4 sampai Akhir:",list)

#Tambah Elemen List
a =[1,2,3,4,5]
b =[6,7,8,9,10]

#Ambil 2 bagian dari list a ke b
b.append(a[1:3])
print("Mengambil bagian list a ke b:",b)
#Menambah list b dengan nilai string
b.append("aduh")
print("Menambah list b dengan nilai string:", b)
#Menambah list b dengan 3 nilai
print("Tambah list b dengan 3 nilai:", b+[20,30,40])
#Menggabungkan list b dengan list a
c=b+a
print("Menggabungkan list a dengan list b:", c)
