from book import Book

while True:

    print("\n==============================")
    print(" Library Management System")
    print("==============================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

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
    # Exit
    # ---------------------------
    elif choice == "3":

        print("\nThank you for using Library Management System!")
        break

    # ---------------------------
    # Invalid Choice
    # ---------------------------
    else:

        print("\nInvalid Choice!")