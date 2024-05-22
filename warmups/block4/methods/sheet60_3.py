for i in range(0, 10):
    text = input()
    while text.count(" ") < 2:
        print("invalid input string")
        text = input()
    
    print(text[text.find(" ") + 1:text.rfind(" ")])