from utils import books

def add():
    book_name = input("Enter the Book name to add: ").upper()
    book_id = int(input ('enter book id :  '))
    books[book_name]=book_id 
    print(f"Book Added: {book_name}")
    