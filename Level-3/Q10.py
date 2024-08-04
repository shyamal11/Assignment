def count_customers_without_computer(N, S):
    computers = N
    occupied = set()
    walked_away = set()
    
    for char in S:
        if char not in occupied:
            if computers > 0:
                occupied.add(char)
                computers -= 1
            else:
                walked_away.add(char)
        else:
            occupied.remove(char)
            computers += 1
    
    return len(walked_away)


N = int(input("Enter the number of computers: "))
S = input("Enter the sequence of arrivals and departures: ")

result = count_customers_without_computer(N, S)
print(result)
