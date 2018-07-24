# define Class petugas
class Gerbong:
    number = 0
    FrontPassenger = 0
    Passenger = 0
    BackPassenger = 0
    Status_pintu = true
    Status_naik_turun = true
    def __init__(self, angka):                                          #Inisialisasi Nomor Gerbong
        self.number = angka;
class Masinis:
    def buka_gerbong():
        return true
class Kereta:
    JumlahGerbong = 0;
    arraylist = []
    def __init__(self, angka):                                          # inisialisasi Jumlah gerbong dalam sebuah KRL
        self.JumlahGerbong = angka
        for i in range(0, self.JumlahGerbong):
            self.arraylist.append(Gerbong(i+1))
    def tanya_gerbong_depan(self, nomor_sekarang):                      #Gerbong x menanyakan jumlah penumpang di depan gerbongnya
        self.arraylist[nomor_sekarang-1].FrontPassenger = self.arraylist[nomor_sekarang-2].Passenger
        return self.arraylist[nomor_sekarang-1].FrontPassenger
    def tanya_gerbong_belakang(self, nomor_sekarang):                   #Gerbong x menanyakan jumlah penumpang di belakagn gerbongnya
        self.arraylist[nomor_sekarang-1].BackPassenger = self.arraylist[nomor_sekarang].Passenger
        return self.arraylist[nomor_sekarang-1].BackPassenger
    def menaikkan_penumpang(self, nomor_sekarang, jumlah):              #Menaikkan penumpang untuk gerbong X dengan jumlah Y
        self.arraylist[nomor_sekarang-1].Passenger += jumlah
    def menurunkan_penumpang(self, nomor_sekarang, jumlah):             #Menurunkan penumpang untuk gerbong X dengan jumlah Y
        self.arraylist[nomor_sekarang-1].Passenger -= jumlah

#ContohEksekusi

KeretaA = Kereta(5)
KeretaA.menaikkan_penumpang(4,3)
KeretaA.menaikkan_penumpang(3,2)
print(KeretaA.tanya_gerbong_sekarang(3))
print(KeretaA.tanya_gerbong_belakang(3))
