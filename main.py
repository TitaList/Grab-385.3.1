#This variable contains path for my file

contact_file = 'data/contact.txt'

def add_contact(): 
      name = input("Enter the name's name:")
      phone = input("Enter the contact's phone number:")

     with open(contact_file, 'a') as f
          f.write(f'{name}:{phone}\n')

    
    print(f'Y'{name} has been add to your contacts!)
    
   
def view_contact():
    print('view contact') 

#Def = define a fuction
# the parens of fuction contain in information
 
    
def main():      
      # while loop will run untile condition run faalse
    # condition 'True' so loop will run forevver untile say stop
    while True:
        print('\nConcact List Application:')
        print('1. Add Contact')
        print('2. View Contacts')
        print('3. Quit')
        choice = input('Enter your choice: ')

        if choice == '1':
            print('Add Contact')
        elif choice == '2':
            print('View Contacts')
        elif choice == '3':
            print('Goodbye')
            break 
        else:
            print('Invalid Choice. Please try again')    
     
     
#TO RUN a fuction: invoking,excution, running

#this sepcific line of code makes sure the fuction is not run upon import
# only run upon calling , not run upon import within another page

 