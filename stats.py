def count_words():
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    numOfWords = file_contents.split()
    print(f"{len(numOfWords)} words found in the document")

def count_characters():
    file_contents = None
    character_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    wordsList = file_contents.lower().split()
    for word in wordsList:
        for char in word:
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    print(character_dict)

def print_report(book_path):
    file_contents = None
    character_dict = {}
    with open(book_path, 'r') as f:
        file_contents = f.read()

    for char in file_contents.lower():
        if char.isalpha():
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1

    sorted_character_dict = dict(sorted(character_dict.items(), key=lambda x: x[1], reverse=True))
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {sum(character_dict.values())} total words
--------- Character Count -------""")
    for char, count in sorted_character_dict.items():
        print(f"{char}: {count}")
    print("============= END ===============") 
