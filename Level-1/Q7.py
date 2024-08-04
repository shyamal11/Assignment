def are_anagrams(string1, string2):
    if len(string1) != len(string2):
        return False
    
    count1 = [0] * 256
    count2 = [0] * 256

    for i in range(len(string1)):
        count1[ord(string1[i])] += 1
        count2[ord(string2[i])] += 1

    for i in range(256):
        if count1[i] != count2[i]:
            return False

    return True

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print(are_anagrams(string1, string2))
