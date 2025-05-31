from stats import num_words, num_letters

def get_book_text(content_path):
    with open(content_path) as f:
        return f.read()

def main():
    path = "./books/frankenstein.txt"
    book_string = get_book_text(path)
    word_count = num_words(book_string)
    letter_count = num_letters(book_string)
    print(f"{word_count} words found in the document")
    print(letter_count)

main()
