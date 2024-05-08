def num_vowels1(text:str) -> int:
    vowels = 0
    
    for i in range(0, len(text)):
        c = text[i] # no enumerate :'(
        if c in "aeiouAEIOU":
            vowels += 1
    
    return vowels


def num_vowels2(text:str) -> int:
    vowels = 0
    
    for i in range(0, len(text)):
        c = text[i]
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
            vowels += 1
    
    return vowels