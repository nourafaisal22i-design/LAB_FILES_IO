import json
from library import librarian


def save_books(library):
    with open("books.json", "w") as file:
        json.dump(library, file, indent=4)


def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


library = load_books()


while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Check Out Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")

        librarian.add_book(library, title, author, isbn)

    elif choice == "2":
        librarian.display_books(library)

    elif choice == "3":
        search = input("Enter book title: ")
        librarian.search_book(library, search)
    elif choice == "4":
        isbn = input("Enter ISBN: ")
        librarian.remove_book(library, isbn)

    elif choice == "5":
        isbn = input("Enter ISBN: ")
        librarian.check_out_book(library, isbn)
    elif choice == "6":
        isbn = input("Enter ISBN: ")
        librarian.return_book(library, isbn)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")