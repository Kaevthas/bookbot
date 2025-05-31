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

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(letter_count):
    sorted_list =[]
    for letter in letter_count:
        sorted_list.append({"char": letter, "num": letter_count[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
