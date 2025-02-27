from stats import sorted,get_num_words,get_characters
import sys

def get_book_text (path):
    with open(path) as o:
        contents = o.read()
    return contents

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_num_words(text)
    print (f"Found {word_count} total words")
    character_dict = get_characters(text)
    dict_sorted = sorted(character_dict)
    for data in dict_sorted:
        for char, count in data.items():
            if char.isalpha():
                print(f"{char}: {count}")

main()