import re

def crossword_cheater(pattern, dictionary_file="words.txt"):
    """
    Finds words matching a pattern where * means unknown.
    Example: th***ly → thickly, thirdly
    """
    regex_pattern = "^" + pattern.replace("*", ".") + "$"
    regex = re.compile(regex_pattern, re.IGNORECASE)

    matches = []
    try:
        with open(dictionary_file, "r") as f:
            for word in f:
                word = word.strip()
                if regex.match(word):
                    matches.append(word)
    except FileNotFoundError:
        print("Error: dictionary file not found.")
        return []

    return matches

if __name__ == "__main__":
    user_pattern = input("Enter word with * for unknown letters: ")
    results = crossword_cheater(user_pattern)
    if results:
        print("Possible words:", ", ".join(results))
    else:
        print("No matches found.")
