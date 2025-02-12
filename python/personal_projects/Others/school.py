# Write this with python
s1 = 1
d1 = 0
d2 = 0
# Burası döngü olmaz
while (s1 <= 5):
    d1 = d1 + s1
    s2 = 1
# Burası bitmeden <- O yüzden önce burası üç'e kadar bitiyor ondan sonra tekrar başlıyor.
    while (s2 <= 3):
        d2 = d1 + s2
        s2 += 1
 # Let's we print like a readbale table
    print ("s1, s2, d1, d2:\n", s1, s2, d1, d2)
    s1 += 1

    