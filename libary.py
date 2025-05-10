def display_menu():
    print("\nLibrary Menu:")
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. Check if a book is available")
    print("4. Sort books alphabetically")
    print("5. Display number of books")
    print("6. Show all books")
    print("0. Exit")

def main():
    library = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            book = input("Enter the book title to add: ")
            library.append(book)
            print(f"'{book}' has been added.")
        
        elif choice == "2":
            book = input("Enter the book title to remove: ")
            if book in library:
                library.remove(book)
                print(f"'{book}' has been removed.")
            else:
                print("Book not found in the library.")

        elif choice == "3":
            book = input("Enter the book title to check: ")
            if book in library:
                print(f"'{book}' is available.")
            else:
                print(f"'{book}' is not available.")

        elif choice == "4":
            library.sort()
            print("Books sorted alphabetically.")

        elif choice == "5":
            print(f"There are {len(library)} book(s) in the library.")

        elif choice == "6":
            print("Books in the library:")
            for b in library:
                print(f"- {b}")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()