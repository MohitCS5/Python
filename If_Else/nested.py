x = int(input("print your number :"))
if x<10:
    print("your number is greater than 30")
    if x<20:
        print("your number is still greater than 30")
        if x <=30:
            print("valid number")
else:
    print("invalid number")

score = 85
attendence = 90
submitted = True
if score >= 60 and attendence >= 80 and submitted:
    print("Pass with good standing")
elif score >= 60 and attendence >= 80 and not submitted:
    print("Pass but missing assignment")
elif score >= 60 and attendence < 80:
    print("Pass but low attendance")
else:
    print("Fail")


username = "Emil"
password = False
is_active = True

if username:
    if password:
        if is_active:
            print("login successful")
        else:
            ("acc is nto active")
    else:
        print("pawword is incorrect")
else:
    print("username is incorrect")
