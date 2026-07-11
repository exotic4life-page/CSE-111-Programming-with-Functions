# Optional enhancement (extra credit / usability):
# - Warns the user if wordlist.txt or toppasswords.txt is missing from the project directory.
#   This does not change the required password-strength logic.

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
           "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">",
           "?", "/", "\\", "", "~"]


def word_in_file(word, filename, case_sensitive=False):
    """
    Reads a file (one word per line) and checks whether `word` exists in it.

    Parameters:
        word (str)
        filename (str)
        case_sensitive (bool) default False

    Return:
        bool
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_word = line.strip()
                if case_sensitive:
                    if word == line_word:
                        return True
                else:
                    if word.lower() == line_word.lower():
                        return True
    except FileNotFoundError:
        # If file isn't found, treat as "not found" (avoid crashing).
        return False

    return False


def word_has_character(word, character_list):
    """
    Returns True if ANY character in `word` exists in `character_list`.
    Otherwise returns False.
    """
    for ch in word:
        if ch in character_list:
            return True
    return False


def word_complexity(word):
    """
    Complexity rating is the number of character types found among:
    LOWER, UPPER, DIGITS, SPECIAL. Range: 0..4
    """
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


def password_strength(password, min_length=10, strong_length=16):
    """
    Checks password against:
    - dictionary word list (case-insensitive)
    - top passwords list (case-sensitive)
    - length rules
    - otherwise: strength = 1 + complexity

    Prints the required message and returns an integer strength (0..5).
    """
    dictionary_filename = "wordlist.txt"
    toppasswords_filename = "toppasswords.txt"

    # Dictionary check (case-insensitive)
    if word_in_file(password, dictionary_filename, case_sensitive=False):
        print("'Password is a dictionary word and is not secure.")
        return 0

    # Top passwords check (case-sensitive)
    if word_in_file(password, toppasswords_filename, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Too short
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Strong length: "longer than 15 characters"
    # If strong_length defaults to 16, then len(password) >= strong_length matches "longer than 15".
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Complexity-based strength
    complexity = word_complexity(password)  # 0..4
    strength = 1 + complexity              # 1..5
    return strength


def main():
    # File names expected in the project directory
    dictionary_filename = "wordlist.txt"
    toppasswords_filename = "toppasswords.txt"

    # Optional enhancement: show warnings if files aren't present.
    import os
    if not os.path.exists(dictionary_filename):
        print(f"Warning: '{dictionary_filename}' not found in the project directory.")
    if not os.path.exists(toppasswords_filename):
        print(f"Warning: '{toppasswords_filename}' not found in the project directory.")

    while True:
        user_password = input("Enter a password to test (or Q to quit): ")

        if user_password == "q" or user_password == "Q":
            print("Quitting password strength checker.")
            break

        strength = password_strength(user_password)
        print(f"Password strength score: {strength}/5")


if __name__ == "__main__":
    main()