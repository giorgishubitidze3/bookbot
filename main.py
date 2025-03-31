from stats import count_words
from stats import count_characters
from stats import print_report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text():
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)



def main():
    print_report(book_path)

main()