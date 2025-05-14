def count_words(txt_file):
    txt_vector = txt_file.split()
    word_count = len(txt_vector)
    return word_count

def count_characters(txt_file):
    char_count = {}  # Initialize an empty dictionary

    for char in txt_file.lower():  # Convert characters to lowercase
        char_count[char] = char_count.get(char, 0) + 1  # Count occurrences
    
    return char_count  # Return the dictionary

def sort_character_counts(char_count):
    # Convert dictionary to a list of dictionaries and filter non-alphabetical characters
    sorted_list = [{"char": char, "num": count} for char, count in char_count.items() if char.isalpha()]
    
    # Sort the list by 'num' in descending order
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    
    return sorted_list

def format_character_counts(sorted_list):
    output = "--------- Character Count -------\n"
    for item in sorted_list:
        output += f"{item['char']}: {item['num']}\n"
    output += "============= END ==============="
    return output