def count_letter(word:str, letter:str) -> int:
    count = 0

    for character in word:
        if character == letter:
            count += 1
    
    return count