def build_histogram(text):
    char_frequency = {}
    for char in text:
        if char.isalnum() or char in ",.!?:-;()":
            char_frequency[char] = char_frequency.get(char, 0) + 1
    sorted_chars = sorted(char_frequency.keys())
    for char in sorted_chars:
        if char == '#':
            count = char_frequency[char]
            print(char + " " + "#" * count)
    for char in sorted_chars:
        if char != '#':
            count = char_frequency[char]
            print(char + " " + "#" * count)

encrypted_text = input()

build_histogram(encrypted_text)