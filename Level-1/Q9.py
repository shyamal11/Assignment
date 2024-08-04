def count_frequencies(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency_count = count_frequencies(input_list)

print(f"Frequency count: {frequency_count}")
