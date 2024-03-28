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
        add_book_read_status = bool(int(add_book_read_status))
        break

    #id
    global last_book_id
    add_book_id = last_book_id + 1
    last_book_id = add_book_id

    return {'id': add_book_id, 'title': add_book_title, 'read_status': add_book_read_status}


# Editing a book
def edit_book(book_dict):
    
    while True:
        # editing title
        input_edit_title = input("Would you like to edit a title?: y or n\n")
        
        if input_edit_title == 'y':
            while True:
                change_title = input("Please input new title: ")

                if change_title == "":
                    print("Book title is empty.")
                    continue
                break

            book_dict['title'] = change_title
            break
        elif input_edit_title == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    while True:
        # editing read status
        input_edit_read_status = input("Would you like to edit a read status?: y or n\n")

        if input_edit_read_status == 'y':
            while True:
                change_read_status = input("Please input new read status: 0(Unread) or 1(Readed)\n")

                if change_read_status not in ['0', '1']:
                    print("Invalid input. Please enter '0' or '1'.")
                    continue
                break

            book_dict['read_status'] = bool(int(change_read_status))
            break
        elif input_edit_read_status == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return book_dict


# Searching a book
def search_book(books_list):
    while True:
        user_input_search_name = input("Please input the word that you want to search.\n")
        if user_input_search_name == "":
            continue
        break

    search_result = []

    for row in books_list:
        if user_input_search_name in row["title"]:
            search_result.append(row)
    
    if len(search_result) == 0:
        print("There are no titles containing " + user_input_search_name + ".")
    elif len(search_result) > 0:
        print("The following is the results.")
        display_all_book(search_result)
    
    return search_result


# Deleting a book
def delete_book(books_list, del_index):
    del books_list[del_index]
    return books_list

# Viewing library stats
def view_lib_stats(books_list):
    # Stats info
    # total books
    # total readed books
    # total unreaded books
    # read ratio (readed / total * 100)
    # all books

    total_books = len(books_list)
    read_books = len([book for book in books_list if book["read_status"] == True])
    unread_books = len([book for book in books_list if book["read_status"] == False])
    read_ratio = read_books / total_books * 100

    print(f"Total books: {total_books}")
    print(f"Read books: {read_books}")
    print(f"Unread books: {unread_books}")
    print(f"Read ratio {read_ratio}%")
    print("-- All book info --")
    display_all_book(books_list)


# Display all book
def display_all_book(books_list):
    # Get column names
    fields = books_list[0].keys()

    # get the max title length
    max_title_length = 5
    for row in books_list:
        title_length = len(row['title'])
        if title_length > max_title_length:
            max_title_length = title_length
    # print(max_title_length)

    # {'id': 9, 'title': maxt_title_length, 'read_status': 11}
    column_length = {'id': 9, 'title': max_title_length, 'read_status': 11}

    # display column names
    for field in fields:
        print(f"{field:<{column_length[field]}}", end=" ")
    print()

    # display data
    for row in books_list:
        for data in row.items():
            print(f"{str(data[1]):<{column_length[data[0]]}}", end=" ")
        print()

# get books list and index from 'id' key
def get_book_index_from_id(books_list, num_string):
    index = 0
    for book in books_list:
        if book["id"] == int(num_string):
            return book, index
        index += 1
    return None


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
            print("Books list is empty. Please add an book to books list.")
            continue

        elif len(books_list) > 0:
            display_all_book(books_list)

            all_keys = str(list(data['id'] for data in books_list))

            while True:
                # chose the id that you want to edit
                user_input_edit_book_id = input("Please choose the ID that you want to edit: ")

                if user_input_edit_book_id in all_keys:
                    edit_book_dict, edit_index = get_book_index_from_id(books_list, user_input_edit_book_id)
                    # print("edit_book_dict", edit_book_dict, "edit_index", edit_index, "type", type(edit_index))
                    # print(books_list[edit_index], type(books_list[edit_index]))
                    edit_book(books_list[edit_index])
                    break
                elif user_input_edit_book_id not in all_keys:
                    print("Invalid input. Please input .")
                    continue

    elif user_input == '3':
        if len(books_list) == 0:
            print("Books list is empty. Please add some books to books list.")
            continue
        elif len(books_list) > 0:
            search_book(books_list)

    elif user_input == '4':
        if len(books_list) == 0:
            print("Books list is empty. Please add some books to books list.")
            continue

        elif len(books_list) > 0:
            display_all_book(books_list)

            all_keys = str(list(data['id'] for data in books_list))

            while True:
                # chose the id that you want to delete
                user_input_delete_book_id = input("Please choose the ID that you want to delete: ")

                if user_input_delete_book_id in all_keys:
                    delete_book_dict, delete_index = get_book_index_from_id(books_list, user_input_delete_book_id)
                    delete_book(books_list, delete_index)
                    print("books_list", books_list)
                    break
                elif user_input_delete_book_id not in all_keys:
                    print("Invalid input. Please input .")
                    continue

    elif user_input == '5':
        if len(books_list) == 0:
            print("Books list is empty. Please add some books to books list.")
            continue

        elif len(books_list) > 0:
            view_lib_stats(books_list)

    elif user_input == '6':
        print("Thank you. Closed.")
        break

    else:
        print("""
****************************************
A number other than 1 to 6 was selected.
****************************************
        """)
