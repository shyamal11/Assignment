def parse_encoded_string(encoded_str):
    parts = encoded_str.split('0')
    first_name = parts[0]
    last_name = parts[1]
    id_value = parts[2]
    return {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_value
    }

encoded_str = input("Enter the encoded string: ")
result = parse_encoded_string(encoded_str)
print(result)
