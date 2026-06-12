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

# Python does not have switch statement
grade = 72
if grade >= 90:
    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print(letter_grade)

grade = 72
if grade >= 90:
    print("Passed with Distinction")
else:
    if grade >= 70:
        print("Passed")
    else:
        print("Failed")

grade = 72
if grade >= 90:
    print("Passed with Distinction")
elif grade >= 70:
    print("Passed")
else:
    print("Failed")

account_enabled = True
balance = 1000
withdraw = 100_000

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

if not account_enabled:
    print("account disabled")
else:
    if withdraw > balance:
        print("insufficient funds")
    else:
        print("authorized")

if not account_enabled:
    print("account disabled")
elif withdraw > balance:
    print("insufficient funds")
else:
    print("authorized")
