def get_book_text(filepath):
        path_to_file = filepath
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)

main()