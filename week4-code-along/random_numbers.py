import random


def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    print()
    append_random_numbers(numbers)
    print("Numbers list after appending one random number:")
    print(f"numbers {numbers}")
    
    print()
    append_random_numbers(numbers, 3)
    print("Numbers list after appending three random numbers:")
    print(numbers)
    
    print()

    # Create a list to store random words.
    words = []

    # Call the append_random_words function
    # to add one random word to the list.
    append_random_words(words)
    print(f"words {words}")

    # Call the append_random_words function
    # to add five random words to the list.
    append_random_words(words, 5)
    print(f"words {words}")


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        numbers_list.append(random_number)


def append_random_words(words_list, quantity=1):
    # A list of words to randomly choose from.
    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]

    # Randomly choose quantity words and append them onto words_list.
    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)


if __name__ == "__main__":
    main()