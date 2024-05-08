from task3_functions import *

MENU = "Test which?\n1. Square Root\n2. Digit Product Sum\n3. Braille\n4. Show All Dominos\n5. Trees\n6. Domino Stack\n7. QUIT\nChoice: "

choice = input(MENU)
while choice != "7":
    
    if choice == "1":
        #-== square_root() ==-
 
        number = float(input("Number to square root: "))
        while number <= 0:
            number = float(input("**Positive** number to square root: "))
        
        
        """
        DO NOT EDIT any code below here for this menu option
        """
        root = square_root(number)
        print(f"Square root of {number} is {root}")
        
        
        
    elif choice == "2":
        #-== digit_product_sum() ==-

        low = int(input("Enter a low number for the range: "))
        while low < 0:
            low = int(input("Enter a **non-negative** low number for the range: "))
        
        high = int(input("Enter a high number for the range: "))
        while high < 0:
            high = int(input("Enter a **non-negative** high number for the range: "))

        
        highest = 0
        highest_product_sum = 0

        step = 1
        if high < low:
            step = -1
        for digit in range(low, high + step, step):
            product_sum = digit_product_sum(digit)
            if product_sum > highest_product_sum:
                highest = digit
                highest_product_sum = product_sum

        print(f"From {low} to {high}, {highest} had the highest digit product sum ({highest_product_sum})") 
        
            

    elif choice == "3":
        #-== text_to_braille() ==-

        braille_menu = "\n1. text to Braille\n2. Braille to text\n--> "
        t_to_b_choice = input(braille_menu)
        while t_to_b_choice != "1" and t_to_b_choice != "2":
            t_to_b_choice = input(braille_menu)

        
        
        """
        DO NOT EDIT any code below here for this menu option
        """
        if t_to_b_choice == '1':
            text = input("Enter text: ")
            braille = text_to_braille(text)
            text = braille_to_text(braille)
            print(f"To Braille: {braille}")
            print(f"Back To Text: {text}")
        else:
            braille = input("Enter Braille: ")
            text = braille_to_text(braille)
            braille = text_to_braille(text)
            print(f"To Text: {text}")
            print(f"Back To Braille: {braille}")
        
        

    elif choice == "4":
        #-== domino_str() ==-
  
        for left_side in range(0, 7):
            for right_side in range(0, 7):
                print(domino_str(left_side, right_side))
        
        
        
    elif choice == "5":
        #-== tree_box() ==-

        size = int(input("Tree size: "))
        while size < 0:
            size = int(input("**Non-negative** tree size: "))
        

        """
        DO NOT EDIT any code below here for this menu option
        """
        tree = tree_box(size)
        print(f"Your size-{size} tree:")
        print(tree)
        


    elif choice == "6":
        #-== domino_stack() ==-

        left = int(input("Base domino left # (1 to 5): "))
        while left < 1 or left > 5:
            left = int(input("Base domino left # (1 to 5): "))
        
        right = int(input("Base domino right # (1 to 5): "))
        while right < 1 or right > 5:
            right = int(input("Base domino right # (1 to 5): "))
        
        
        points = int(input("Enter a target number of points: "))
        while left <= 0:
            left = int(input("Enter a **positive** target number of points: "))
        
        

        """
        DO NOT EDIT any code below here for this menu option
        """
        results = (domino_stack(left, right, points))
        print(results)

        
    choice = input("\n"+MENU)