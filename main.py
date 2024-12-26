from company_objects import Person, Customer, Employee

def display_person(person):
    if isinstance(person, Customer):
        print("\nCUSTOMER")
        print("Full name: " + person.full_name())
        print("Email: " + person.email)
        print("Number: " + person.phone_number)
    elif isinstance(person, Employee):
        print("\nEMPLOYEE")
        print("Full name: " + person.full_name())
        print("Email: " + person.email)
        print("SSN: " + person.ssn)

def main():
    print("Customer/Employee Data Entry")
    while True:
        choice = input("Customer or employee? (c/e): ")
        
        print("\nDATA ENTRY")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")

        if choice == 'c':
            phone_number = input("Number: ")
            person = Customer(first_name, last_name, email, phone_number)
        elif choice == 'e':
            ssn = input("SSN: ")
            person = Employee(first_name, last_name, email, ssn)
        else:
            print("Wrong option try again")
        
        display_person(person)
        
        continue_option = input("\nContinue? (y/n): ")
        if continue_option != 'y':
            break

    print("Bye!")

if __name__ == "__main__":
    main()
