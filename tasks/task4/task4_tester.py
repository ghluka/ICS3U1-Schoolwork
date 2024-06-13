from task4_functions import *

choice = input("Test which?\n1. get closest\n2. get proper divisors\n3. number analysis\n4. rolling averages\n5. all adjacent average\n6. align strings\n7. cards!\n8. QUIT\nChoice: ")
while choice != "8":
    
    if choice == "1":
        #-== get_closest() ==-

        '''** DONE FOR YOU! DO NOT EDIT THE FOLLOWING LINES**'''

        closest_choice = input("1. closest to a target\n2. closest pair\nChoice: ")
        
        if closest_choice == "1":
                
            print("Enter a list of integers, such as [1, 45, -3, 78, -10, 0, 12]:")
            values = eval(input(">>>:"))
            
            key = int(input("Enter an integer you wish to find the closest to: "))
            
            print(f"Closest to {key} is {get_closest(values, key)}")


        elif closest_choice == "2":
            #-== get_closest_pair() ==-
    
            '''** DONE FOR YOU! DO NOT EDIT THE FOLLOWING LINES**'''
           
            print("Enter a list of integers, such as [1, 45, -3, 78, -10, 0, 12]:")
            values1 = eval(input(">>>:"))
    
            print("Enter a second list of integers with the same number of integers:")
            values2 = eval(input(">>>:"))
            while len(values2) != len(values1):
                print(f"The second list must have {len(values1)} values")
                values2 = eval(input(">>>:"))
            
            closest_pair = get_closest_pair(values1, values2)
            print(f"Closest pair is {closest_pair[0]} and {closest_pair[1]}")
        
        
    elif choice == "2":
        #-== get_proper_divisors() ==-
        
        '''** DONE FOR YOU! DO NOT EDIT THE FOLLOWING LINES**'''

        number = int(input("What whole number do you want the divisors of? "))
        while number <= 0:
            number = int(input("What POSITIVE whole number do you want the divisors of? "))
        print(f"The proper divisors of {number} are {get_proper_divisors(number)}")    
        

    elif choice == "3":
        #-== number analysis() ==-

        low = int(input("What is the lowest number in the range? "))
        while low <= 0:
            low = int(input("It must be positive, try again: "))

        high = int(input("What is the highest number in the range? "))
        while high <= low:
            high = int(input(f"Must be higher than {low}: "))
        
        abudant = []
        perfect = []
        deficient = []
        prime = []

        for i in range(low, high + 1):
            proper_divisors = get_proper_divisors(i)
            if len(proper_divisors) == 1 and proper_divisors[0] == 1:
                prime.append(i)
            if sum(proper_divisors) > i:
                abudant.append(i)
            elif sum(proper_divisors) == i:
                perfect.append(i)
            else:
                deficient.append(i)

        print(f"In the numbers from {low} to {high}:")
        print(f"-> {len(abudant)} are abundant: {abudant}")
        print(f"-> {len(perfect)} are perfect: {perfect}")
        print(f"-> {len(deficient)} are deficient: {deficient}")
        print(f"-> {len(prime)} are prime: {prime}")

        
    elif choice == "4":
        #-== rolling_averages() ==-
                
        '''** DONE FOR YOU! DO NOT EDIT THE FOLLOWING LINES**'''
        
        print("Enter a list of integers, such as [1, 45, -3, 78, -10, 0, 12]:")
        values = eval(input(">>>:"))

        size = int(input("How big should the chunks be? "))
        
        while size < 1 or size > len(values):
            if size < 1:
                size = int(input("Chunk size must be positive: "))
            else:
                size = int(input("Chunk size cannot be larger than the list: "))
        
        print(f"Averages: {rolling_averages(values, size)}")
    
    
    
    elif choice == "5":
        #-== all adjacent average ==-

        print("Enter a list of integers, such as [1, 45, -3, 78, -10, 0, 12]:")
        values = eval(input(">>>:"))
        avg = sum(values) / len(values)

        while len(values) != 1:
            values = rolling_averages(values, 2)

        print(f"All adjacent average: {values[0]}")
        print(f"Actual average: {avg}")


    elif choice == "6":
        #-== align_strings() ==-
        
        '''** DONE FOR YOU! DO NOT EDIT THE FOLLOWING LINES**'''
        try:
            file_name = input("Enter the name of a text file to use as input: ")
            text_file = open(file_name)
            text_list = text_file.read().split("\n")
            key = input("Enter a string to align to: ")
            while key == "":
                key = input("Enter a string to align to: ")
                
            aligned = align_strings(text_list, key)
            if aligned == "":
                print(f"'{key}' was not anywhere in that file")
            else:
                print(aligned)
        except FileNotFoundError as e:
            print(f"File '{file_name}' does not exist")
        

    elif choice == "7":
        #-== cards ==-

        '''** DONE FOR YOU! DO NOT EDIT THE FOLLOWING LINES**'''

        num_decks = int(input("How many decks would you like: "))
        while num_decks <= 0:
            num_decks = int(input("Enter a positive number: "))
        cards = make_decks(num_decks)

        card_choice = input("\nCard Menu:\n1. cut the cards\n2. shuffler\n3. deal cards\n4. see cards\n5. QUIT\nChoice: ")

        while card_choice != "5":
            if card_choice == "1":
                # cut the deck
                if len(cards) == 1:
                    print("Cannot cut 1 card")
                else:
                    cut_the_cards(cards)
                    print("Done!")

            elif card_choice == "2":
                # shuffle the deck
                if len(cards) == 1:
                    print("Cannot shuffle 1 card")
                else:
                    cards = shuffler(cards)
                    print("Done!")

            elif card_choice == "3":
                # deal cards
                num_cards = int(input("How many cards to deal? "))
                while num_cards <= 0:
                    num_cards = int(input("Enter a positive number: "))
                hand = deal_n_cards(cards, num_cards)
                print(f"{len(hand)}-cards dealt: {hand}")

            elif card_choice == "4":
                # see cards
                if cards == "[]":
                    print("No cards left")
                else:
                    cards_copy = cards.copy()
                    while len(cards_copy) > 0:
                        print("  ".join(cards_copy[:10]))
                        cards_copy = cards_copy[10:]

            card_choice = input("\nCard Menu:\n1. cut the cards\n2. shuffler\n3. deal cards\n4. see cards\n5. QUIT\nChoice: ")
                
        
    choice = input("\nTest which?\n1. get closest\n2. get proper divisors\n3. number analysis\n4. rolling averages\n5. all adjacent average\n6. align strings\n7. cards!\n8. QUIT\nChoice: ")