# Adding a book
def add_book():
    # title
    while True:
        add_book_title = input("Please input the book title.\n")

        if add_book_title == "":
            print("Book title is empty.")
            continue
        break

    # read_status
    while True:
        add_book_read_status = input("Please select 0(Unread) or 1(Readed).\n")

        if add_book_read_status != '0' and add_book_read_status != '1':
            print("A number other than 0 or 1 was selected.")
            continue
        break

    #id
    global last_book_id
    add_book_id = last_book_id + 1
    last_book_id = add_book_id

    return {'id': add_book_id, 'title': add_book_title, 'read_status': add_book_read_status}


# Editing a book
def edit_book(book):
    # editing title
    input_edit_title = input("Would you like to edit a title?: y or n\n")
    
    while True:
        if input_edit_title == 'y':
            change_title = input("Please input new title: ")

            while True:
                if change_title == "":
                    print("Book title is empty.")
                    continue
                break

            book['title'] = change_title
            break
        elif input_edit_title == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
    # editing read status
    input_edit_read_status = input("Would you like to edit a read status?: y or n\n")

    while True:
        if input_edit_read_status == 'y':
            change_read_status = input("Please input new read status: 0(Unread) or 1(Readed)\n")

            while True:
                if change_read_status not in ['0', '1']:
                    print("Invalid input. Please enter '0' or '1'.")
                    continue
                break

            book['read_status'] = change_read_status
            break
        elif input_edit_read_status == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return


# Searching a book
def search_book():
    pass

# Deleting a book
def delete_book():
    pass

# Viewing library stats
def view_lib_stats():
    pass

# Display first message
def display_first_message():
    print("""
================================================
Welcome to your personal books digital library!
================================================
1: Add a Book
2: Edit a Book
3: Search for Books
4: Delete a Book
5: View Library Stats
6: Exit app
        """)



# Booklist is initialized as empty list.
books_list = []

# Global variable
last_book_id = 0

# book1 = {'id': 1, 'title': 'AAA', 'read_status': False}
# book2 = {'id': 2, 'title': 'BBB', 'read_status': True}
# book3 = {'id': 3, 'title': 'CCC', 'read_status': False}

while True:
    display_first_message()
    user_input = input("Please select from 1 to 6\n")

    if user_input == '1':
        books_list.append(add_book())
        print(books_list)
    elif user_input == '2':
        if len(books_list) == 0:
            print("Books list is empty. Please add some books to books list.")
            continue

        edit_book(books_list[0])
        print(books_list)
    elif user_input == '3':
        search_book()
    elif user_input == '4':
        delete_book()
    elif user_input == '5':
        view_lib_stats()
    elif user_input == '6':
        print("Thank you. Closed.")
        break
    else:
        print("""
****************************************
A number other than 1 to 6 was selected.
****************************************
        """)
