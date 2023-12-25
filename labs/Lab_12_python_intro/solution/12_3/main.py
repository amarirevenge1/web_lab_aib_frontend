def generate_histogram(text):
    char_count = {}

    for char in text:
        if char != ' ' and char != '\n':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    sorted_chars = sorted(char_count.items(), key=lambda x: (ord(x[0])))

    max_count = max(char_count.values())

    histogram = ''
    for i in range(max_count, 0, -1):
        line = ''
        for char, count in sorted_chars:
            if count >= i:
                line += '#'
            else:
                line += ' '
        histogram += line + '\n'

    symbols = ''.join([char for char, _ in sorted_chars])
    histogram += symbols


    with open('output.txt', 'w') as file:
        file.write(histogram)



with open('input.txt', 'r') as file:
    encrypted_text = file.read()


generate_histogram(encrypted_text)
