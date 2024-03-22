from task1_functions import *

menu = "Test which?\n1. near sine\n2. Easter date\n3. age difference\n4. seconds converter\n5. QUIT!\nChoice: "

choice = input(menu)
while choice != "5":
    
    if choice == "1":

        degrees = float(input('How many degrees are in your angle: '))



        siney = near_sine(degrees)



        print(f"sin({degrees}) = {siney:.4f} based on pi={near_pi()}")
        
        
        
    elif choice == "2":

        year = int(input('What year would you like to find Easter for: '))



        easter = easter_date(year)



        print(f"Easter {year} is on {easter}")
        
        
        
    elif choice == "3":

        name1 = input('What is the name of your first person: ')
        age1 = int(input('What is the first person\'s age? '))
        name2 = input('What is the name of your second person: ')
        age2 = int(input('What is the second person\'s age? '))
        


        diff = age_difference(name1, age1, name2, age2)
        print(diff)
        
        
        
    elif choice == "4":

        seconds = int(input('How many seconds do you want to convert: '))
        


        nicer = seconds_converter(seconds)
        
        
        
        print(f"{seconds} seconds is really {nicer}!")
        

    choice = input("\n"+menu)