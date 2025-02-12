def calculate_final_grade(vize):
    grades = {
        "AA": 85,
        "AB": 78,
        "BA": 72,
        "BB": 67,
        "BC": 62,
        "CB": 57,
        "CC": 51,
        "CD": 47,
        "DC": 41,
        "DD": 34,
        "FF": 1
    }

    for grade, score in grades.items():
        final = (score - (vize * 0.30)) / 0.70
        print(f"To get a {grade}, you need to get a final grade of at least: {final}")

# Example usage
calculate_final_grade(30)