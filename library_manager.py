from book import Book

while True:

    print("\n==============================")
    print(" Library Management System")
    print("==============================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ---------------------------
    # Add Book
    # ---------------------------
    if choice == "1":

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)

        # Save book to file
        file = open("books.txt", "a")
        file.write(book_id + "," + title + "," + author + ",Available\n")
        file.close()

        print("\nBook Added Successfully!\n")
        book.display()

    # ---------------------------
    # View Books
    # ---------------------------
    elif choice == "2":

        file = open("books.txt", "r")
        books = file.readlines()
        file.close()

        if len(books) == 0:
            print("\nNo books found.\n")

        else:
            print("\nBook Details\n")

            for book in books:

                data = book.strip().split(",")

                print("------------------------")
                print("Book ID :", data[0])
                print("Title   :", data[1])
                print("Author  :", data[2])
                print("Status  :", data[3])
                print()

    # ---------------------------
    # Search Book
    # ---------------------------
    elif choice == "3":

        search_id = input("Enter Book ID to search: ")

        file = open("books.txt", "r")
        books = file.readlines()
        file.close()

        found = False

        for book in books:

            data = book.strip().split(",")

            if data[0] == search_id:

                print("\nBook Found\n")
                print("------------------------")
                print("Book ID :", data[0])
                print("Title   :", data[1])
                print("Author  :", data[2])
                print("Status  :", data[3])
                print()

                found = True
                break

        if not found:
            print("\nBook not found.\n")

    # ---------------------------
    # Delete Book
    # ---------------------------
    elif choice == "4":

        delete_id = input("Enter Book ID to delete: ")

        file = open("books.txt", "r")
        books = file.readlines()
        file.close()

        found = False

        file = open("books.txt", "w")

        for book in books:

            data = book.strip().split(",")

            if data[0] != delete_id:
                file.write(book)
            else:
                found = True

        file.close()

        if found:
            print("\nBook deleted successfully!\n")
        else:
            print("\nBook not found.\n")

    # ---------------------------
    # Exit
    # ---------------------------
    elif choice == "5":

        print("\nThank you for using Library Management System!")
        break

    # ---------------------------
    # Invalid Choice
    # ---------------------------
    else:

        print("\nInvalid Choice!")