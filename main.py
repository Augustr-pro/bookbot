from stats import count_words
from stats import count_characters
from stats import sort_character_counts
from stats import format_character_counts

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text('books/frankenstein.txt')
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {count_words(book_text)} total words')
    char_count = count_characters(book_text)
    print(format_character_counts(sort_character_counts(char_count)))

main()