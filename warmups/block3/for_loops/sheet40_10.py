def count_letters(word:str, letters:str) -> int:
    count = 0

    for character in word:
        for letter in letters:
            if character == letter: 
                count += 1
    
    return count