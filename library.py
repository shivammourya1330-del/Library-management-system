# LIBRARY
books = []
issued_books = []
# ADD BOOKS 
def add_books():
    name = input("Enter the books name :")
    books.append(name)
    print("Books added")

# SHOW BOOKS 
def show_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("Books available.")
        for b in books:
            print(b)

# ISSUE BOOKS
def issue_books():
    name = input("Enter the books name:")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Books Issued")
    else:
        print("Books not issued.")

# RETURN BOOKS
def return_books():
    name = input("Enter the books name :") 
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("Books returned.")
    else:
        print("Not returned.")
        
# MAIN BODY
def library():
    while True:
        print("-------------------")
        print("1.Add Books")
        print("2.Show Books")
        print("3.Issue Books")
        print("4.Return")
        print("5.Exit")
        print("-------------------")
        choice = int(input("Enter your choice :"))

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank You")
            break
library()