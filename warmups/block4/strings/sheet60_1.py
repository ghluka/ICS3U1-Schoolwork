def num_vowels3(text:str) -> int:
    text = text.lower()
    
    vowels = 0
    for vowel in "aeiou":
        vowels += text.count(vowel)
        
    return vowels