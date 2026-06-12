if 1 < 2:
    print("1 is less than 2")

if 1 > 2:
    print("block - line 1")
    print("block - line 2")
    print("block - line 3")
print("next line")


if 1 > 2:
    print("1 is greater than 2")
else:
    print("1 is not greater than 2")

account_enabled = True
balance = 1000
withdraw = 100

if account_enabled and withdraw <= balance:
    print("authorized")
else:
    if not account_enabled:
        print("account disabled")
    else:
        print("insufficient funds")
    print("not authorized")

grade = 72
if grade >= 90:
    letter_grade = "A"
else:
    if grade >= 80:
        letter_grade = "B"
    else:
        if grade >= 70:
            letter_grade = "C"
        else:
            if grade >= 60:
                letter_grade = "D"
            else:
                lletter_grade = "F"
print(letter_grade)

grade = 72
if grade >= 90:
    letter_grade = "A"
if grade >= 80 and grade < 90:
    letter_grade = "B"
if grade >= 70 and grade < 80:
    letter_grade = "C"
if grade >= 60 and grade < 70:
    letter_grade = "D"
if grade < 60:
    letter_grade = "F"
print(letter_grade)


grade = 72
letter_grade = "F"
if grade >= 60:
    letter_grade = "D"
if grade >= 70:
    letter_grade = "C"
if grade >= 80:
    letter_grade = "B"
if grade >= 90:
    letter_grade = "A"
print(letter_grade)
