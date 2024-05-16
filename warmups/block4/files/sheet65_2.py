def count_letter_in_file(path:str, letter:str) -> int:
    in_file = open(path)
    occurrences = in_file.read().count(letter)
    in_file.close()
    
    return occurrences