# This variable contains the path for your file
contact_file = 'data/contact.txt'

def add_contact(): 
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")

    # Standard 4-space indentation for the 'with' block
    with open(contact_file, 'a') as f:
        f.write(f'{name}: {phone}\n')

    print(f'{name} has been added to your contacts!')

def view_contact():
    try:
        with open(contact_file, 'r') as f:
            contacts = f.readlines() # Changed 'contact' to 'contacts' to match the loop below
             
            if not contacts:
                print('Your contact list is empty.')
            else:
                print('--- Your Contact List ---') 
                for contact in contacts: # Added the missing colon here
                    print(contact, end='') # Removed extra space for cleaner output 
             
    except FileNotFoundError:
        print('Your contact list is empty (file not found).')

def main():      
    while True:
        print('\nContact List Application:')
        print('1. Add Contact')
        print('2. View Contacts')
        print('3. Quit')
        choice = input('Enter your choice: ')

        if choice == '1':
            add_contact() # Call the actual function
        elif choice == '2':
            view_contact() # Call the actual function
        elif choice == '3':
            print('Goodbye!')
            break 
        else:
            print('Invalid Choice. Please try again.')

# Standard way to run the program
# Standard way to run the program
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    
    
    
        
    