letter_map = {
    'a': 2,
    'b': 3,
    'c': 5,
    'd': 7, 
    'e': 11, 
    'f': 13, 
    'g': 17, 
    'h': 19, 
    'i': 23, 
    'j': 29, 
    'k': 31, 
    'l': 37, 
    'm': 41, 
    'n': 43, 
    'o': 47, 
    'p': 53, 
    'q': 59, 
    'r': 61, 
    's': 67, 
    't': 71, 
    'u': 73, 
    'v': 79, 
    'w': 83, 
    'x': 89, 
    'y': 97, 
    'z': 101
}

def is_anagram(word1, word2):
    """
    Check if two words are anagrams of each other.
    
    Args:
        word1 (str): The first word.
        word2 (str): The second word.
    
    Returns:
        bool: True if the words are anagrams, False otherwise.
    """
    def normalize(letter):
        return letter_map[letter]

    anagram1 = 1
    anagram2 = 1

    for letter in word1:
        anagram1 = anagram1 * normalize(letter)

    for letter in word2:
        anagram2 = anagram2 * normalize(letter)

    return anagram1 == anagram2

def main():
    print(is_anagram('listen', 'silent'))  # True
    print(is_anagram('hello', 'world'))    # False
    print(is_anagram('evil', 'vile'))      # True
    print(is_anagram('fluster', 'restful')) # True

if __name__ == "__main__":
    main()