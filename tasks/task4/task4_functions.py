"""Provides solutions for the 8 functions in Task 4's assignment 
"""

__author__ = "Luka"
__date__ = "2024/06/10"


def get_closest(values:list, target:int) -> int:
    closest = values[0]

    for v in values:
        if abs(target - v) < abs(target - closest):
            closest = v
    
    return closest


def align_strings(strings:list, substr:list) -> list:
    closest_i = 0

    if len(strings) != len(substr):
        return []
    
    for i in range(0, len(strings)):
        if abs(substr[i] - strings[i]) < abs(substr[closest_i] - strings[closest_i]):
            closest_i = i
            
    return [strings[closest_i], substr[closest_i]]


def get_proper_divisors(number:int) -> list:
    return []


def rolling_averages(values:list, size:int) -> list:
    return []


def align_strings(strings:list, substr:list) -> str:
    return ""


def make_decks(num_decks: int) -> str: # provided by assignment
    '''
    Return a list of 2-character cards for num_decks standard card decks,
    ordered by value (A to K) and suit (♠, ♣, ♥, ♦).
    '''
    deck = []

    for c in 'A23456789TJQK':
        for s in '♠♣♥♦':
            deck.extend([f'{c}{s}']*num_decks)

    return deck


def deal_n_cards(cards:list, n:int) -> list:
    return []


def cut_the_cards(cards:list):
    return None
    

def shuffler(values:list) -> list:
    return []


#-----------------------------------------------------------------------------
if __name__ == "__main__": # provided by assignment
    '''
    Below is all testing code from the handout's given test cases.
    Uncomment the sets of tests as you complete the functions in order
    to test your own results.
    '''

    #numbers = [5, 9, 0, -3, 15, 8, 4]
    #print(get_closest(numbers, 10))	 
    
    
    #numbers1 = [5, 9, 0, -3, 15, 8, 4]
    #numbers2 = [12, 13, 8, 2, 0, 11, -1]
    #print(get_closest_pair(numbers1, numbers2))	
    #print(get_closest_pair(numbers1, [1, 2, 3]))	
    
    
    #print(get_proper_divisors(12))
    #print(get_proper_divisors(29)) 
    #print(get_proper_divisors(1))
    
    
    #numbers = [3, 9, 2, 10, 14, 20, 13]
    #print(rolling_averages(numbers, 2))	
    #print(rolling_averages(numbers, 4))	 
    #print(rolling_averages(numbers, 10))	 

    
    #lines = ["Computer", "Science", "is", "a challenge", "for MANY", "people"]
    #print(align_strings(lines, "e"))
    #words = ["mathematics", "radius", "theorem", "breathe", "apothem", "area"]
    #print(align_strings(words, "The"))
    
    
    #decks = make_decks(1)
    #hand = deal_n_cards(decks, 8)
    #print(len(hand), len(decks))
    #print(hand)
    #print(decks)
    
    
    #cards = ['T♣', 'A♠', '7♥', '4♣', '3♦', 'K♦', 'K♥', '5♣']
    #cut_the_cards(cards)
    #print(cards) 
    #cut_the_cards(cards)
    #print(cards)
    
    
    #cards = ['T♣', 'A♠', '7♥', '4♣', '3♦', 'K♦', 'K♥', '5♣']
    #cards = shuffler(cards)
    #print(cards)
    
    
    #cards = ['T♣', 'A♠', '7♥', '4♣', '3♦', 'K♦', 'K♥', '5♣']
    #cards = shuffler(cards)
    #print(cards)