# takes the book string and splits it into words, returning the count of words
def num_words(text):
    return len(text.split())

# takes the book string and counts the number of letters, returning a dictionary
def num_letters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# a helper function to sort the dictionaries by the "num" key
def sort_on(dict):
    return dict["num"]

# takes the letter count dictionary and returns a sorted list of dictionaries from highest to lowest
def dict_to_sorted_list(letter_count):
    sorted_list =[]
    for letter in letter_count:
        sorted_list.append({"char": letter, "num": letter_count[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
