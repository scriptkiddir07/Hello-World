nama = "Hermawan Ramadhani"
umur = 13
bb = 65
alamat = "yogyakarta"
panjang = 9,5
data_bool = False
data_boool = True
data_complex = complex(5,1)
print "Identitas Lengkap Hr."
print "nama = ", nama
print "umur = ", umur
print "bb = ", bb
print "alamat = ", alamat
print "panjang = ", panjang
print (type(umur))
print (type(panjang))
print (type(nama))
print (type(data_boool))
print (type(data_bool))
print (type(data_complex))

from ctypes import c_double

data_double = c_double(1.2)

print (type(data_double))