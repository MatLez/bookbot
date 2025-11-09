# Get word_count, character count and list function from stats.py
from stats import word_count, get_characters, sort_dict
import sys
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

# Get book and print it
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)

# Give filepath and call get_book
def main(filepath):
    sorted_characters = sort_dict(get_characters(filepath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    word_count(filepath)
    print("--------- Character Count -------")
    for i in sorted_characters:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main(filepath)