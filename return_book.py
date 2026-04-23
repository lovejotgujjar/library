from utils import issue_books, books

def return_book():
    book_name = input("Enter book name: ").upper()
    if book_name in issue_books:
        book_id = issue_books[book_name]
        issue_books.pop(book_name)
        books[book_name]= book_id
        print("Book returned")
    else:
        print("blablabla")
        