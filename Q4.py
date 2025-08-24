# CALCCULATE GRADE :
def cal_grade(marks):
    if marks >= 90:
        return "Ex"
    elif marks >=80:
        return "A"
    elif marks >=70:
        return "B"
    elif marks >=60:
        return "C"
    else:
        return "F"  
    
you = map(int, input("Enter the marks: ").split())
marks = sum(you)
print("Grade:", cal_grade(marks))