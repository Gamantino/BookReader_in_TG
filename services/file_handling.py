BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    chars = (".", ",", "!", "?", ":", ";")
    end = start + size if len(text) > (start + size) else len(text)
    while end != len(text):
        last_char = text[end - 1]
        if last_char in chars and not text[end] in chars:
            break
        end -= 1
    return text[start:end], len(text[start:end])


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding="utf-8") as my_book:
        text = my_book.read()
    num_page = 1
    start = 0
    while True:
        page, len_text = _get_part_text(text, start, PAGE_SIZE)
        if page == '':
            break
        page = page.lstrip()
        book[num_page] = page
        num_page += 1
        start += len_text


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
