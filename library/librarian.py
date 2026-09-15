def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }

        print("Book added successfully.")

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("Book removed successfully.")
    else:
        print("Book not found.")

def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found.")

    elif library[isbn]["available"] == False:
        print("Book is already checked out.")

    else:
        library[isbn]["available"] = False
        print("Book checked out successfully.")


def return_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
    else:
        library[isbn]["available"] = True
        print("Book returned successfully.")

def display_books(library):
    if not library:
        print("The library is empty.")
        return

    for book in library.values():
        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(
            f'{book["title"]} by {book["author"]} '
            f'(ISBN: {book["isbn"]}) - {status}'
        )

def search_book(library, search):
    for book in library.values():
        if search.lower() in book["title"].lower():
            print(book)
            return

    print("Book not found.")