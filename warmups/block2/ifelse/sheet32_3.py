def thumbs(thumb_1:str, thumb_2:str) -> str:
    '''Returns a string stating if two players won or lost a game of Thumbs based on which thumb two people play ("r" being right, "l" being left). 
    '''
    if thumb_1.lower() == thumb_2.lower():
        return "WIN"
    return "LOSE"