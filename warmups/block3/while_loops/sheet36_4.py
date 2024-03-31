def thumbs(thumb_1:str, thumb_2:str) -> str:
    '''Returns a string stating if two players won or lost a game of Thumbs based on which thumb two people play ("r" being right, "l" being left).'''
    if thumb_1.lower() == thumb_2.lower():
        return "WIN"
    return "LOSE"


if __name__ == "__main__":
    # Player 1 using loop method 1
    thumb_1 = input("Player 1 > enter a thumb (L for left or R for right): ")
    while thumb_1.lower() != "l" and thumb_1.lower() != "r":
        thumb_1 = input("Player 1 > enter a thumb: ")

    # Player 2 using loop method 2
    thumb_2 = input("Player 2 > enter a thumb (L for left or R for right): ")
    while not (thumb_2.lower() == "l" or thumb_2.lower() == "r"):
        thumb_2 = input("Player 2 > enter a thumb: ")

    print(f"You {thumbs(thumb_1, thumb_2)}!")