from utils import books, issue_books

def issue():
    print ('1.  from book id')
    print ('2.  from book name')
    choice = int(input('enter your choice :  '))
    if choice == 2:
        book_name = input("Enter book name: ").upper()
        if book_name in books:
            book_id = books[book_name]
            books.pop(book_name)
            issue_books[book_name]=book_id
            print("Book assigned successfully")
        else:
            print("Book not available")
    if choice == 1:
        book_id = int(input ('enter your book id :  '))
        if book_id in books.values():
            for key, value in books.items():
                if value == book_id:
                    book_name = key 
                    break
            books.pop(book_name)
            issue_books[book_name]=book_id
            print('book issueed sucessfully  \n')