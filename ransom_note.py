def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Build a hash table (dictionary) to count character frequencies in magazine
    char_count = {}
    for char in magazine:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Check if each character in ransomNote is available in the hash table
    for char in ransomNote:
        # If character is missing or count is depleted, return False early
        if char not in char_count or char_count[char] == 0:
            return False
        # Decrement the count as we "use" this character
        char_count[char] -= 1

    # All characters in ransomNote were found with sufficient frequency
    return True
