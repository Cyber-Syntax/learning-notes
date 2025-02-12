# işletme ilkeleri 51.250
# işlem tablosu 65
# sistem analizi 28.750
# bilgi toplumu ve e-devlet 33.750
# üretim yönetimi 42.500
# kullanıcı deneyimi 51.250
# kurumsal kaynak planlama 38.750


# 24.12.2022
# The program that finds the final grade required to pass the final
# Written by CyberSyntax
# License GPL.
# vize 0.30, final 0.70

# user_Point ;
# 84,00-100 – AA (geçti)
# 77,00-83,99 – AB (geçti)
# 71,00-76,99 – BA (geçti)
# 66,00-70,99 – BB (geçti)
# 61,00-65,99 – BC (geçti)
# 56,00-60,99 – CB (geçti)
# 50,00-55,99 – CC (geçti)
# 46,00-49,99 – CD (Genel Not Ortalaması: 2.00’nin üstündeyse geçer)
# 40,00-45,99 – DC (Genel Not Ortalaması: 2.00’nin üstündeyse geçer)
# 33,00-39,99 – DD (Genel Not Ortalaması: 2.00’nin üstündeyse geçer)
# 0-32,99 – FF (kaldı)
# final  = (50 - vize_Avarage) / 0.70
import math

user_Point = 51

user_Point_BB = 67
def user_Points():
    
    AA = 85 
    AB = 78
    BA = 72
    BB = 67
    BC = 62
    CB = 57
    CC = 51
    CD = 47
    DC = 41
    DD = 34
    FF = 1
    
    return AA, AB, BA, BB, BC, CB, CC, CD, DC, DD, FF

def main():
    vize = get_vize()
    final(vize)

# coefficient = katsayı
def final(vize): 
    # When you want to define variable other defination. # # If you didn't want to define everytime, 
    # you can write "global AA" in user_points 
    AA, AB, BA, BB, BC, CB, CC, CD, DC, DD, FF = user_Points()
    # Kullanıcı nesnesinin value özelliğini kullanarak geçme puanını hesaplayın
    final_CC = (CC - (vize * 0.30)) / 0.70   
    final_BB = (BB - (vize * 0.30)) / 0.70   
    print("To get CC, you need to get final at least: ", final_CC)
    print("to get BB, yo need to get final at least: ", final_BB)

def get_vize():
    return int(input("Vize point: "))

if __name__ == "__main__":
    main()

# vize = 30
# final = 60
# user_Point = 51