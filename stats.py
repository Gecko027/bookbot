def word_count(book_text):
    '''
    Takes a string, and returns word count.    
    :param book_text: Takes a book or text as a string
    return: integer
    '''
    words = book_text.split()
    count = 0
    for word in words:
        count += 1
    return count

def character_count(book_text):
    '''
    Takes a string, and returns the character count.
    :param book_text: Takes a book or text as a string
    return: dictionary
    '''
    characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    final_characters = {

    }
    
    index = 0
    for character in characters:
        count = 0
        for letter in book_text:
            if letter == characters[index]:
                count += 1

        final_characters[characters[index]] = count
        index += 1    

    return final_characters

# Helpe function to extract the "num" key for sorting commparison
def get_num(dictionary):
    return dictionary["num"]


def sort_char(dictionary):
    '''
    Takes a dictionary and sorts it into a list of dictionaries.
    :param dictionary: A Dictionary.
    return: A list of dictionaries.
    '''
    dictionary_list = []
    for key, value in dictionary.items():
        value_two = value
        value_one = key
        key_one = "char"
        key_two = "num"
        new_dictionary = {
            key_one: value_one,
            key_two: value_two
        }
        dictionary_list.append(new_dictionary)
    dictionary_list.sort(reverse=True, key=get_num)
    return dictionary_list

