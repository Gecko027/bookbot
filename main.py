from stats import word_count
from stats import character_count
from stats import sort_char
import sys

def get_book_text(filepath):
    '''
    Take a filepath, and return contents as a string.
    :param filepath: Takes a filepath
    return: string
    '''
    with open(filepath) as f:
        return f.read()
    

def main():
    
    # Sets the system arguments for main.py
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_text = sys.argv[1]

    # Gets the book text
    book_text = get_book_text(path_to_text)
    # Makes all letters in text lowercase
    book_text = book_text.lower()
    # Prints Book Report!!!
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_text}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    
    # Gets the sorted character count and returns list of dictionarys
    text_dictionarys = (sort_char(character_count(book_text)))

    for dict in text_dictionarys:
        print(f"{dict["char"]}: {dict["num"]}")
        

main()