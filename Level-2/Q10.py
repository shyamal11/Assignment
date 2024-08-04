def find_stone_piles(n):
    piles = []
    if n % 2 == 0:
        start = 2
    else:
        start = 1
    current = start
    while current < n:
        piles.append(current)
        current += start
    return piles

n = int(input("Enter the number of stones: "))

stone_piles = find_stone_piles(n)

print(f"Stones in each pile = {stone_piles}")
