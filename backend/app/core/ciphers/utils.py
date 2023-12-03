from ..english_dict import ENGLISH_DICTIONARY
import string


def is_likely_english(text: str) -> bool: 
    """
    Returns true if the given text is likely to be english.

    Args:
        text (str): The text to check.

    Returns:
        bool: True if the given text is likely to be english.
    """
    num_of_english_words = 0
    num_of_words = len(text.split())
    for word in text.split():
        # remove punctuation, special characters, numbers
        word = word.translate(str.maketrans('', '', string.punctuation)).lower()
        if word in ENGLISH_DICTIONARY:
            num_of_english_words += 1                
    
    if (num_of_english_words / num_of_words) >= 0.5: 
        return True
    return False