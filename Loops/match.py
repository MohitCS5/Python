command = "stop"
match command:
    case "start":
        print("starting")
    case "stop":
        print("stopping")
    case "pause":
        print("pausing")
    case _:
        print("value unknown")

#same code with if statement
command = False
if command == True:
    print("you are eligible")
elif command == False:
    print("you are not eligible")
else:
    print("wrong credentials")

#combining value through or operator or (|)
day = 2
match day:
    case 1|2|3|5:
        print("weather was good")
    case 9|8:
        print("weather was bad")

#case with if condition
day =2
month = 2
match day:
    case 1| 2| 4 if month == 2:
        print("holiday in february")
    case 4 | 5 if month == 4:
        print("no holiday")
    case _:
        print("unknown")