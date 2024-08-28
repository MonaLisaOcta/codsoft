names = []
contact_numbers = []
num = int(input("Enter the limits of contacts you want to save: "))
for i in range(num):
    name = input("please enter the Name: ")
    contact_number = int(input("please enter the Contact Number: ")) 
    names.append(name)
    contact_numbers.append(contact_number)
print("\nName\t\t\tContact Number\n")
for i in range(num):
    print("{}\t\t\t{}".format(names[i], contact_numbers[i]))
search_term = input("\nEnter the contact you want to search: ")
print("Search result:")
if search_term in names:
    index = names.index(search_term)
    contact_number = contact_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, contact_number))
else:
    print("No records have been found")
    