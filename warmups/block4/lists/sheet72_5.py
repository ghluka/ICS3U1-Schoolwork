def words(text:str) -> list:
    all_words = text.upper().split(",")
    all_words.sort()
    return all_words