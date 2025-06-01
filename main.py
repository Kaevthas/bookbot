import sys
from stats import (
    num_words,
    num_letters,
    dict_to_sorted_list
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    book_string = get_book_text(path)
    word_count = num_words(book_string)
    letter_count = num_letters(book_string)
    sorted_list = dict_to_sorted_list(letter_count)
    print_result(path, word_count, sorted_list)

# opens the book file from a path and reads the eniter content into a string
def get_book_text(content_path):
    with open(content_path) as f:
        return f.read()
    
def print_result(path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count --------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
