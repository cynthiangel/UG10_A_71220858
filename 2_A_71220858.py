print ("==== Selamat datang di Toko Andi Tersenyum, selamat belanja ====")

a = int(input( "Total belanja :Rp. "))
b = a-a*2/100
c = a-a*5/100
d = a-(a*10/100)

if a >= 1000000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", d)
elif a >= 500000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", c)
elif a >= 100000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", b)
else :
    print (" Tidak ada diskon ! Maka yang anda bayarkan adalah : ", a)
