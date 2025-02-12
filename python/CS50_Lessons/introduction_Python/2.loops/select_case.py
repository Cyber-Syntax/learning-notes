# from open_ai

def get_grade(score):
  grade = 'F'
  if score >= 90:
    grade = 'A'
  elif score >= 80:
    grade = 'B'
  elif score >= 70:
    grade = 'C'
  elif score >= 60:
    grade = 'D'
  return grade

print(get_grade(92))  # prints 'A'
print(get_grade(84))  # prints 'B'
print(get_grade(70))  # prints 'C'
print(get_grade(50))  # prints 'D'
print(get_grade(40))  # prints 'F'
