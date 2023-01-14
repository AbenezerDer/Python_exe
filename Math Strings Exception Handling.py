while True:
    
    try:
         number = int(input("please enter a number : "))
         break

    except ValueError:
        print("you didn't enter a number")

    except:
        print("An unknown error occured")
        
print("Thank you for entering a number")