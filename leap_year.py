#this program is going to determine if a year is a leap
def leap():
    
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                print("{} is a leap year.".format(user_year))
            else:
                print("{} is not a leap year.".format(user_year))
        else:
            print("{} is a leap year.".format(user_year))
    else:
        print("{} is not a leap year.".format(user_year))
        
leap()
user_year = int(input("Please Enter Your Year: "))
