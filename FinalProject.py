print(' WELCOME TO THE LIBRARY SYSTEM '.center(100, '~'))


class Book:
    def __init__(self, book_id, title, author, level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.level = level
        self.available = True

    def __str__(self):
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\n" \
               f"Level: {self.level}\nAvailability: {'Available' if self.available else 'Not available'}\n"


class Member:
    def __init__(self, member_id, name, email, level):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    def __str__(self):
        books_str = ""
        if self.borrowed_books:
            books_str = "\n".join([f"- {book.title}" for book in self.borrowed_books])
        else:
            books_str = "No books borrowed"
        return f"Member ID: {self.member_id}\nName: {self.name}\nEmail: {self.email}\n" \
               f"Level: {self.level}\nBorrowed Books:\n{books_str}\n"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def edit_member(self, member_id):
        member = self.find_member_by_id(member_id)
        if member is None:
            print("Invalid member ID.")
            return

        print(f"Editing member: {member.name}")
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        level = input("Enter Level : ")

        if name:
            member.name = name
        if email:
            member.email = email
        if level:
            member.level = level

        print("Member information updated successfully.")

    def display_members(self):
        print(" List of Members ".center(31, '*'))
        for member in self.members:
            print(f'ID | {member.member_id}, Name | {member.name}, Email | {member.email} ,Level | {member.level}')

    def delete_member(self, member_id):
        member = self.find_member_by_id(member_id)

        if member is None:
            print("Invalid member ID.")
            return

        self.members.remove(member)
        print(f"{member.name} has been successfully deleted.")

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(" List of Books ".center(30, '*'))
        for book in self.books:
            print(f'ID | {book.book_id}, Title | {book.title}, Author | {book.author} ,Level | {book.level}, '
                  f'Status | {"Available" if book.available else "Not available"}')

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def edit_book(self, book_id):
        edited_book = self.find_book_by_id(book_id)
        if edited_book is None:
            print("Invalid Book ID.")
            return

        print(f"Editing Book: {edited_book.title}")
        edited_book_name = input("Enter Book Name: ")
        edited_book_author = input("Enter Author: ")
        edited_book_level = input("Enter Level: ")

        if edited_book_name:
            edited_book.title = edited_book_name
        if edited_book_author:
            edited_book.author = edited_book_author
        if edited_book_level:
            edited_book.level = edited_book_level

        print("Book information updated successfully.")

    def borrow_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if member is None or book is None:
            print("Invalid member ID or book ID.")
            return

        if book.available and member.level >= book.level:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{book.title} has been successfully borrowed by {member.name}.")
        elif not book.available:
            print(f"{book.title} is not available for borrowing.")
        else:
            print(f"{member.name} is not eligible to borrow {book.title}.")

    def return_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if member is None or book is None:
            print("Invalid member ID or book ID.")
            return

        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.available = True
            print(f"{book.title} has been successfully returned by {member.name}.")
        else:
            print(f"{member.name} did not borrow {book.title}.")


library = Library()

while True:
    try:
        choice = int(input("\n1. Add Member\n2. Edit Member\n3. Show Members\n4. Delete Member\n5. Add Book\n"
                           "6. Edit Books\n7. Show Books\n8. Borrow Book\n9. Return Book\n10. Exit"
                           "\n Enter your choice: "))

    except:
        print("Invalid input!! Please enter a number..!")
        continue

    if choice == 1:
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        level = input("Enter Level (A/B/C): ").upper()
        member = Member(member_id, name, email, level)
        library.add_member(member)
        print("Member added successfully!")

    elif choice == 2:
        member_id = input("Enter Member ID to edit: ")
        library.edit_member(member_id)

    elif choice == 3:
        library.display_members()

    elif choice == 4:
        member_id = input("Enter Member ID to delete: ")
        library.delete_member(member_id)

    elif choice == 5:
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        level = input("Enter Level (A/B/C): ").upper()
        book = Book(book_id, title, author, level)
        library.add_book(book)
        print("Book added successfully!")

    elif choice == 6:
        member_id = input("Enter Member ID to edit: ")
        library.edit_book(book_id)

    elif choice == 7:
        library.display_books()

    elif choice == 8:
        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")
        library.borrow_book(member_id, book_id)

    elif choice == 9:
        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")
        library.return_book(member_id, book_id)

    elif choice == 10:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")