import json

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title":self.title,
            "author":self.author,
            "is_issued":self.is_issued
        }
    
    @staticmethod
    def from_dict(data):
        book = Book(data["book_id"], data["title"], data["author"])
        book.is_issued = data["is_issued"]
        return book




class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = {}
        self.load_from_file()

    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists. Try another ID.")
            return
        self.books[book.book_id] = book

    def show_books(self):
        for book in self.books.values():
            status = "Issued" if book.is_issued else "Available"
            print(f"ID: {book.book_id} | {book.title} | {book.author} | {status}")

    def search_books(self, keyword):
        found = False
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                status = "Issued" if book.is_issued else "Available"
                print(f"ID: {book.book_id} | {book.title} | {book.author} | {status}")
                found = True

        if not found:
            print("No Book Found.")

    def issue_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.is_issued:
                book.is_issued = True
                self.save_to_file()
                print("Book issued successfully.")
            else:
                print("This book is already issued.")

        else:
            print("Book ID not found.")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_issued:
                book.is_issued = False
                self.save_to_file()
                print("Book returned successfully.")
            else:
                print("This book was not issued.")
        else:
            print("Book ID not found.")
    
    def report(self):
        total_books = len(self.books)
        issued_books = 0

        for book in self.books.values():
            if book.is_issued:
                issued_books += 1
        
        print("Total books:", total_books)
        print("Issued books:", issued_books)

    def save_to_file(self):
        data = {}
        for book_id, book in self.books.items():
            data[book_id] = book.to_dict()

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Library saved to file.")

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)


            for book_id, book_data in data.items():
                book = Book.from_dict(book_data)
                self.books[int(book_id)] = book

            print("Library loaded from file.")

        except FileNotFoundError:
            print("No saved library file found. Starting with empty library.")

        except json.JSONDecodeError:
            print("Library file is corrupted. Startingwith empty library.")






def menu():
    print("\n=========== Library Book Inventory Manager =============")
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Report")
    print("7. Save & Exit")




lib = Library()

while True:
    menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        book = Book(book_id, title, author)
        lib.add_book(book)
        print("Book added successfully.")

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        keyword = input("Enter title or author to search: ")
        lib.search_books(keyword)

    elif choice == "4":
        book_id = int(input("Enter Book ID to issue: "))
        lib.issue_book(book_id)

    elif choice == "5":
        book_id = int(input("Enter Book ID to return: "))
        lib.return_book(book_id)
    
    elif choice == "6":
        lib.report()

    elif choice == "7":
        lib.save_to_file()
        print("Library saved. Exiting...")
        break

    else:
        print("Invalid choice. Please select between 1 to 7.")

