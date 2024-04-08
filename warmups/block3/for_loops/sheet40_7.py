n = int(input("How big do you want your chart to be: "))
for x in range(1, n + 1):
    for y in range(1, n + 1):
        print(f"  {x * y: >{len(str(n ** 2))}}", end="")
    print()