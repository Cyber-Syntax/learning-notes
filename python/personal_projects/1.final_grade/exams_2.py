# işletme ilkeleri          51.25 Final = 49.47
# işlem tablosu             65    Final = 43.58 
# sistem analizi            28.75 Final = 59.12
# bilgi toplumu ve e-devlet 33.75 Final = 56.97
# üretim yönetimi           42.5  Final = 53.22
# kullanıcı deneyimi        51.25 Final = 49.47
# kurumsal kaynak planlama  38.75 Final = 54.83


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
from math import ceil

def main():
    vize = get_vize()
    calculate_final_grade(vize)

# coefficient = katsayı
# In order not to put the students at risk, 1 point higher grade point is taken as the basis.
# TODO, tam sayı dene
def calculate_final_grade(vize):
    grades = {
        "AA": 84.01,
        "AB": 77.01,
        "BA": 71.01,
        "BB": 66.01,
        "BC": 61.01,
        "CB": 56.01,
        "CC": 50.01,
        "CD": 46.01,
        "DC": 40.01,
        "DD": 33.01,
        "FF": 1.01
    }

    for grade, score in grades.items():
        final = (score - (vize * 0.30)) / 0.70
        #ceil_final = ceil(final) # round high number just in case.
        print(f"To get a {grade}, you need to get a final grade of at least: {final}")
    
def get_vize():
    return float(input("Vize point: "))

if __name__ == "__main__":
    main()
