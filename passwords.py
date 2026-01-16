#no extra steps because I couldn't even get the Top Passwords and Word List items to work right...

from pathlib import Path

LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?",
    "/", "`", "~"
]


ABS_DICT = Path("/Users/conta/Documents/BYU Pathway/CSE 111/Week 2/wordlist.txt")
ABS_TOP  = Path("/Users/conta/Documents/BYU Pathway/CSE 111/Week 2/toppasswords.txt")

BASE_DIR = Path(__file__).parent
REL_DICT = BASE_DIR / "wordlist.txt"
REL_TOP  = BASE_DIR / "toppasswords.txt"

DICTIONARY_FILE = ABS_DICT if ABS_DICT.exists() else REL_DICT
TOPPASSWORDS_FILE = ABS_TOP if ABS_TOP.exists() else REL_TOP


def word_in_file(word, filename, case_sensitive=False) -> bool:
 
    try:
        path = Path(filename)
        with path.open("r", encoding="utf-8") as f:
            if case_sensitive:
                target = word
                for line in f:
                    if target == line.strip():
                        return True
            else:
                target = word.lower()
                for line in f:
                    if target == line.strip().lower():
                        return True
        return False
    except FileNotFoundError:
        # If the file is missing, act as "not found" so program still runs.
        return False


def word_has_character(word, character_list) -> bool:
  
    for ch in word:
        if ch in character_list:
            return True
    return False


def word_complexity(word) -> int:
  
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


def password_strength(password, min_length=10, strong_length=16) -> int:
   
    # 1) Dictionary (case-insensitive)
    if word_in_file(password, DICTIONARY_FILE, case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # 2) Common passwords (case-sensitive)
    if word_in_file(password, TOPPASSWORDS_FILE, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3) Too short
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4) Long wins
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # 5) Complexity path
    comp = word_complexity(password)  # 0..4
    return 1 + comp  # 1..5


def main():
    print("Password Strength Checker (enter Q to quit)")
    while True:
        pw = input("Enter a password to test: ").strip()
        if pw.lower() == "q":
            print("Goodbye.")
            break
        score = password_strength(pw)
        print(f"Strength: {score}/5")


if __name__ == "__main__":
    main()