def num_words(text):
    return len(text.split())

def num_letters(words):
    char_count = {}
    for char in words.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
