def display_menu():
    print("Shopping List Manager")
    print('1. Add item')
    print('2. Remove item')
    print('3. View list')
    print('4. Exit')

def main():
    shopping_list=[]
    while True:
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 1:
            item = input('Enter item to add: ')
            shopping_list.append(item)
        elif choice == 2:
            item = input('Enter item to remove: ')
            if item in shopping_list:
                shopping_list.remove(item) 
            else:
                print('Item not found')
        elif choice == 3:
            print('Shopping list:')
            for item in shopping_list:
                print(item)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Kindly read the options and try again.")

if __name__ == '__main__':
    main()                                