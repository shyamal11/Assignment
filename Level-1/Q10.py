def reverse_words(sentence):
    words = []
    start = 0
    
    for i in range(len(sentence)):
        if sentence[i] == ' ' or i == len(sentence) - 1:
            if i == len(sentence) - 1:
                end = i + 1
            else:
                end = i
            
            words.append(sentence[start:end])
            start = i + 1
    
    reversed_sentence = ''
    for i in range(len(words) - 1, -1, -1):
        reversed_sentence += words[i]
        if i != 0:
            reversed_sentence += ' '
    
    return reversed_sentence

input_sentence = "Hello, World! Welcome to Python programming."
reversed_sentence = reverse_words(input_sentence)

print(f"Output after reverse = \"{reversed_sentence}\"")
