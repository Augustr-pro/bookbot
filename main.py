def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def count_words(txt_file):
    txt_vector = txt_file.split()
    word_count = len(txt_vector)
    return word_count

def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(f'{count_words(book_text)} words found in the document')

main()