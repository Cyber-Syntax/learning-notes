# The program that finds the final grade required to pass the final of the course whose midterm grade is known
# Written by CyberSyntax
# Created on 24.12.2022

# Türkiye AOF grade points:
# 84,00-100 – AA (passed)
# 77,00-83,99 – AB (passed)
# 71,00-76,99 – BA (passed)
# 66,00-70,99 – BB (passed)
# 61,00-65,99 – BC (passed)
# 56,00-60,99 – CB (passed)
# 50,00-55,99 – CC (passed)
# 46,00-49,99 – CD (GPA: Pass if above 2.00)
# 40,00-45,99 – DC (GPA: Pass if above 2.00)
# 33,00-39,99 – DD (GPA: Pass if above 2.00)
# 0-32,99 – FF (failed to pass)
# midterm 0.30, final 0.70 taken basis.

# TODO, test this notes

# Real 
# Midterm, Final, Başarı notu
# 51.250 , 48.750 49.500 BC
# 51.250 , 57.500 55.625 BB
# 65.000 , 77.500 73.750 BA
# 28.750 , 16.250 20.000 FF
# 42,500   30,000 33,750 FF
# 38,750   28,750 31,750 FF
# 33,750   52,500 46,875 CB
# !

import math
# TODO, add some comments
def main():
    grade = Grade()           
    grade.calculate_final_grade(grade.get_midterm())

class Grade:    
    def calculate_final_grade(self, midterm):
        # TODO later, change CC inputable like CC = 60 etc.
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
        # TODO, add GPA grade requirement 
        # TODO, change midterm and final avarage inputable
        # TODO later, kredi notu öğrenip eklenebilir
        for grade, score in grades.items():
            final = (score - (midterm * 0.30)) / 0.70        
            print(f"To get a {grade}, you need to get a final grade of at least: {final}")
    
    
    def get_midterm(self):
        # TODO, add exceptions
        midterm = float(input("midterm point: ").title())
        return midterm

    #def get_final_avarage
     
    #def get_midterm_avarage
     
    #def get_CC_grade 
    #find to handle when CC added 60 what can we do about that.    

if __name__ == "__main__":
    main()
