print("What do you want to know about me?")
ques = int(input("1. Name 2. age 3. hobby 4. birthday"))

match ques:
    case 1:
        print("My name is Khang")
    case 2:
        print("Turning 19 this year")
    case 3:
        print("I like playing badminton and games")
    case 4:
        print("My birthday is 26th April")
    case 5:
        print("You hate your life, don't you?")

for i in range(0,10):
    print("Anything else you want to know?")
    decision = int(input("1. yes 2. no"))
    if decision == 1:
        print("What's more do you want to know about me?")
        ques = int(input("1. Name 2. age 3. hobby 4. birthday"))

        match ques:
            case 1:
                print("My name is Khang")
            case 2:
                print("Turning 19 this year")
            case 3:
                print("I like playing badminton and games")
            case 4:
                print("My birthday is 26th April")
            case 5:
                print("You hate your life, don't you?")
    else:
        print("Have a great day!")
        exit()