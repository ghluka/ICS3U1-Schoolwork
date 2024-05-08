def text_shuffle1(text:str) -> str:
    """text_shuffle() using indexing"""
    for i in range(4):
        even = ""
        odd = ""

        for i in range(0, len(text)):
            if i % 2 == 0:
                even += text[i]
            else:
                odd += text[i]

        text = f"{even}{odd}"

    return text


def text_shuffle2(text:str) -> str:
    """text_shuffle() using slicing"""
    for _ in range(4):
        text = f"{text[::2]}{text[1::2]}"

    return text