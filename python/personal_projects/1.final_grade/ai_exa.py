import math

class UserPoint:
    # This is for self default value when user didn't give value.
    def __init__(self, value):
        self.value = value
# cleared code from(resource: conditionals/grade.py)
    def get_grade(self):
        if 84 <= self.value <= 100:
            return "AA"
        elif self.value >= 83.99:
            return "AB"
        elif self.value >= 76.99:
            return "BA"
        elif self.value >= 70.99:
            return "BB"
        elif self.value >= 65.99:
            return "CC"
        elif self.value >= 49.99:
            return "CD"
        elif self.value >= 45.99:
            return "DC"
        elif self.value >= 39.99:
            return "DD"   
        elif 0 <= self.value <= 32.99:
            return "FF"
    # TODO clear this to
    def get_passing_score(self):
        if 84 <= self.value <= 100:
            return 0
        elif 77 <= self.value <= 83.99:
            return 1
        elif 71 <= self.value <= 76.99:
            return 2
        elif 66 <= self.value <= 70.99:
            return 3
        elif 50 <= self.value <= 65.99:
            return 4
        elif 46 <= self.value <= 49.99:
            return 5
        elif 40 <= self.value <= 45.99:
            return 6
        elif 33 <= self.value <= 39.99:
            return 7                
        elif 0 <= self.value <= 32.99:
            return 8


def main():
    
    # Define get_vize (resource: exceptions/hello_2.py)
    vize = get_vize("Write your vize point: ")
       
    # TODO, define get_user_point
    get_user_point(vize)

# TODO, this defining didn't finish because of vize name error
def get_user_point(vize):
    # UserPoint sınıfından tüm değerler için nesneler oluşturun
    user_points = [UserPoint(value) for value in range(46,65)]

    cc_values = []
    for user_point in user_points:        
        final_Score = final(vize, user_point)
        print(f"To get {user_point.get_grade()}, you need to get at least: {final_Score:.2f}")               
        #final_score = final(vize, user_point)    
        # TODO, name 'vize' is not defined for each word points. 
        # this is just lining passing scores. 
        # CC                
        # if 49.99 <= final_score <= 65.99:
        #     cc_values.append(user_point.get_grade())
        #     print(cc_values)        
        # else:
        #     print("Unknow error")
        #     break
        

def get_vize(prompt):
    # TODO, add while true str error handling(resource: conditionals/if.py and exceptions/)
    return int(input(prompt))


def get_vize_avarage(vize):
    return (vize * 0.30)

def final(vize, user_point):  
    return (user_point.value - get_vize_avarage(vize)) / 0.70    
   

    
if __name__ == "__main__":
    main()