"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list, or at 
    preferred order after first item."""
    list_item = 'What item do you want to add to your list? '    
    item = (raw_input(list_item)).lower()
    if item in my_list:
        print item + ' is already in the list'
    elif len(my_list) == 0:
        my_list.insert(0, item)
        print "\nYour first item, " + item + ", was added successfully"
    else:
        list_position = '\n \n And where in the list do you want this item to be added? (Type a number > 1)\n '''
        position = raw_input(list_position)
        my_list.insert((int(position)-1), item)
        

        print item + " added successfully" 

    display_main_menu(my_list)
   


def view_list(my_list):
    """Print each item in the list."""
    print 'To do List: \n'
    for index, item in enumerate(my_list, 1):
        print index, item

    display_main_menu(my_list)
 


def edit_item(my_list):
    '''Prints current items and takes user input on which item (index) should be 
    replaced. Takes user input on what to replace it with'''
    print 'These are the items in your list'
    for index, item in enumerate(my_list, 1):
        print index, item
    old_item = '\nPlease type the index of the item to be edited: \n'
    old_item_index = int(raw_input(old_item)) - 1
    new_item = 'What do you want to replace it with? '
    new_item_input = (raw_input(new_item)).lower()
    my_list[old_item_index] = new_item_input

    display_main_menu(my_list)



def delete_item(my_list):
    '''Prints current list and takes user input (string) on which item to delete '''
    print '\nThere are the items in your list:'
    for i in my_list:
        print '\n' + i + '\n', 

    item = raw_input('\nWhich item of the list you want to delete? ')

    if item in my_list:
        number = my_list.index(item)

        my_list.pop(number)    

        print '\n' + item + ' was deleted from the list'
    else:
        print 'This item is not listed'

    display_main_menu(my_list)
    


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Edit an item
    D. Remove an item 
    E. Quit the program
    >>> """
     
    
    while True:
        choice = raw_input(user_options)
        if choice.upper() == 'A':
            return add_to_list(my_list)
        elif choice.upper() == 'B':
            return view_list(my_list)
        elif choice.upper() == 'C':
            return edit_item(my_list)
        elif choice.upper() == 'D':
            return delete_item(my_list)
        elif choice.upper() == 'E':
            break 
        else:
            print "Invalid Option"
            return display_main_menu(my_list)

#-------------------------------------------------


my_list = []
display_main_menu(my_list)

