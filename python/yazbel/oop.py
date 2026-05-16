class Çalışan:
    kabiliyetleri = []
    unvanı = "işçi"
    maaşı = 1500
    memleketi = ""
    doğum_tarihi = ""


ahmet = Çalışan()
mehmet = Çalışan()
ayşe = Çalışan()

print("ahmet kabiliyetleri:", ahmet.kabiliyetleri)
print(ahmet.unvanı)

print(mehmet.maaşı)
print(mehmet.memleketi)

print(ayşe.kabiliyetleri)
print(ayşe.doğum_tarihi)


ahmet.kabiliyetleri.append("prezantabl")
print("ahmet kabiliyetleri(+prezantabl):", ahmet.kabiliyetleri)

selim = Çalışan()

print("selim kabiliyetleri:", selim.kabiliyetleri)
print("Ayşe kabiliyetleri:", ayşe.kabiliyetleri)
