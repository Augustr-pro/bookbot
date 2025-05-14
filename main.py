from stats import count_words
from stats import count_characters

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(f'{count_words(book_text)} words found in the document')
    char_count = count_characters(book_text)
    print(char_count)

main()