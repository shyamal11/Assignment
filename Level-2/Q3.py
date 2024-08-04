def count_pairs(arr, k):
    count = 0
    seen = set()
    for num in arr:
        complement = k - num
        if complement in seen:
            count += 1
        seen.add(num)
    return count

arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
k = int(input("Enter the value of K: "))

pair_count = count_pairs(arr, k)

print(f"Pair count: {pair_count}")
