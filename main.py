def main() -> None:

    BOOK_PATH = "books/frankenstein.txt"
    text = get_book_text(BOOK_PATH)
    num_words = count_words(text)
    char = count_letters(text)
    print(f"{num_words=} in the document")
    print(char)


def count_words(text: str) -> int:
    word_list = text.split()
    return len(word_list)


def count_letters(text: str) -> dict[str, int]:
    char_dic: dict[str, int] = {}
    for char in text.lower():
        if char not in char_dic:
            char_dic[char] = 1
        else:
            char_dic[char] += 1
    return char_dic


def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()


if __name__ == "__main__":
    main()
