import sys
from stats import get_num_words, get_char_count, sort_char_count


def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    # Word count
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    char_count = get_char_count(text)
    sorted_chars = sort_char_count(char_count)

    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

