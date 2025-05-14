def count_words(txt_file):
    txt_vector = txt_file.split()
    word_count = len(txt_vector)
    return word_count

def count_characters(txt_file):
    char_count = {}  # Initialize an empty dictionary

    for char in txt_file.lower():  # Convert characters to lowercase
        char_count[char] = char_count.get(char, 0) + 1  # Count occurrences
    
    return char_count  # Return the dictionary