def num_vowels3(text:str) -> int:
    text = text.lower()
    
    vowels = text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")

    return vowels