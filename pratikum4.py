pelanggan="Budi Santoso"
totalBelanja=150000

if(totalBelanja > 100000):
    keterangan="selamat anda mendapat hadiah"

else:
    keterangan="terimakasih sudah berbelanja"

print("pelanggan",pelanggan,"\n Total Belanja Anda Rp.",totalBelanja,"\n",keterangan)

nama="budi"
matpel="matematika"
nilai=59.99
keterangan="lulus" if nilai >=60 else "gagal"

print("nama\t:",nama,"\nmatpel\t:",matpel,"\nnilai\t\t:",nilai,"\nketerangan\t:",keterangan)

nama="santoso"
matpel="matematika"
nilai=60

if(nilai >=85 and nilai <=100):
    grade="A"
elif(nilai >=75 and nilai <=85):
    grade="B"
elif(nilai >=60 and nilai <=75):
    grade="C"
elif(nilai >=30 and nilai <=60):
    grade="D"
else:
    grade="E"

print("nama\t:",nama,"\nmatpel\t:",matpel,"\nnilai\t\t:",nilai,"\ngrade\t:",grade )


