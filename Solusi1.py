# define Class petugas
class Gerbong:
    number = 0
    FrontPassenger = 0
    Passenger = 0
    BackPassenger = 0
    Status_penumpang = 1                                                # 0 = selesai, 1 = belum
    def __init__(self, angka):                                          # Inisialisasi Nomor Gerbong
        self.number = angka
    def jumlah_penumpang(self):
        return self.Passenger
    def jumlah_penumpang_depan(self):
        return self.FrontPassenger
    def jumlah_penumpang_belakang(self):
        return self.BackPassenger
    def naik_penumpang(self, angka):
        self.Passenger += angka
    def turun_penumpang(self, angka):
        self.Passenger -= angka
    def set_penumpang_depan(self, angka):
        self.FrontPassenger = angka
    def set_penumpang_belakang(self, angka):
        self.BackPassenger = angka
    def naik_turun_selesai(self):
        self.Status_penumpang = 0
    def mulai_naik_turun(self):
        self.Status_penumpang = 1
    def cek_naik_turun(self):
        return self.Status_penumpang
class Masinis:
    status_pintu = 0                                                    # 0 = buka, 1 = tutup
    def __init__(self):
        self.status_pintu = 0
    def tutup_pintu(self):
        self.status_pintu = 1
    def buka_pintu(self):
        self.status_pintu = 0
    def status_gerbong(self):
        return self.status_pintu
class Kereta:
    JumlahGerbong = 0;
    arraylist = []
    TandaGerbong = []
    naik_penumpang_terakhir = 0;                                        # menandakan gerbong terakhir yang belum selesai menaikkan penumpang
    gerbong_masinis = Masinis()                                         # 0 = Penumpang naik turun, 1 =
    def __init__(self, angka):                                          # Inisialisasi Jumlah gerbong dalam sebuah KRL
        self.JumlahGerbong = angka
        self.gerbong_masinis.buka_pintu()
        naik_penumpang_terakhir = angka-1
        for i in range(0, self.JumlahGerbong):
            self.arraylist.append(Gerbong(i+1))                         # MEngupdate jumlah penumpang dari depan gerbong X
    def tanya_gerbong_depan(self, nomor_sekarang):
        self.arraylist[nomor_sekarang-1].set_penumpang_depan(self.arraylist[nomor_sekarang-2].jumlah_penumpang())
        return self.arraylist[nomor_sekarang-1].jumlah_penumpang_depan()
    def tanya_gerbong_belakang(self, nomor_sekarang):                   # Mengupdate jumlah penumpang dari belakang gerbong X
        self.arraylist[nomor_sekarang-1].set_penumpang_belakang(self.arraylist[nomor_sekarang].jumlah_penumpang())
        return self.arraylist[nomor_sekarang-1].jumlah_penumpang_belakang()
    def menaikkan_penumpang(self, nomor_sekarang, jumlah):              # Menaikkan penumpang untuk gerbong X dengan jumlah Y
        self.arraylist[nomor_sekarang-1].naik_penumpang(jumlah)
    def menurunkan_penumpang(self, nomor_sekarang, jumlah):             # Menurunkan penumpang untuk gerbong X dengan jumlah Y
        self.arraylist[nomor_sekarang-1].turun_penumpang(jumlah)
    def tanya_gerbong_sekarang(self, nomor_sekarang):
        return self.arraylist[nomor_sekarang-1].jumlah_penumpang()
    def naik_turun_selesai(self, nomor_sekarang):                       # Menandakan gerbong x telah selesai menaikkan penumpang.
        self.arraylist[nomor_sekarang-1].naik_turun_selesai()
        while (self.naik_penumpang_terakhir >-1) and (self.arraylist[self.naik_penumpang_terakhir].cek_naik_turun() != 1):
            self.naik_penumpang_terakhir -=1
        if (self.naik_penumpang_terakhir < 0):
            self.gerbong_masinis.tutup_pintu()
    def status_pintu_gerbong(self):
        return self.gerbong_masinis.status_gerbong()
    def buka_gerbong(self):
        self.gerbong_masinis.buka_pintu()
        for i in range(0, self.JumlahGerbong):
            self.arraylist[i].mulai_naik_turun()
        self.naik_penumpang_terakhir = self.JumlahGerbong-1

#ContohEksekusi

KeretaA = Kereta(3)
KeretaA.buka_gerbong()
KeretaA.menaikkan_penumpang(3,2)
print(KeretaA.tanya_gerbong_sekarang(3)) # Jumlah penumpang gerbong 3
print(KeretaA.tanya_gerbong_belakang(2)) # Jumlah penumpang belakang gerbong 2
print(KeretaA.status_pintu_gerbong())   # status pintu gerbong saat ini
KeretaA.naik_turun_selesai(2)

print(KeretaA.status_pintu_gerbong())
KeretaA.naik_turun_selesai(1)
print(KeretaA.status_pintu_gerbong())
KeretaA.naik_turun_selesai(3)
print(KeretaA.status_pintu_gerbong())
