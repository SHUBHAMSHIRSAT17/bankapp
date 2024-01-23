import sys

print(
    "----------------------------------------------------------------Welcome to your "
    "bank app---------------------------------------------------------------------------")


class Bank:
    def __init__(self, name, branch, account_no, age, mobile_no, salary):
        self.name = name
        self.branch = branch
        self.account_no = account_no
        self.age = age
        self.mobile_no = mobile_no
        self.salary = salary
        self.amount = 0

    def enquiry(self):
        print("Customer Details:")
        print("Bank Name is:-", self.name)
        print("Branch Name is:-", self.branch)
        print("Your Account Number is:-", self.account_no)
        print("Your Age is:-", self.age)
        print("Your Mobile Number is:-", self.mobile_no)

    def deposit(self, amount):
        self.amount += amount
        print("Amount Successfully Deposit", self.amount)

    def withdraw(self, amount):
        if self.amount - amount >= 5000:
            self.amount -= amount
            print("Amount Successfully Withdraw")
        else:
            print("Insufficient Balance.\nYou have to keep at least Rs.5000 in your bank account")

    def display(self):
        print("Your Balance is ", self.amount, "\n")

    def apply_for_loan(self, principal, annual_interest_rate, loan_period):
        if self.age >= 25:
            print(f"Congratulations! Your loan of Rs.{principal} has been approved.")
            self.amount += principal
            monthly_interest_rate = (annual_interest_rate / 100) / 12
            loan_period_months = loan_period * 12
            emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_period_months) / (
                    (1 + monthly_interest_rate) ** loan_period_months - 1)

            print(emi)
        else:
            print("Sorry, you are not eligible for a loan at this time.")


bank_object = []


def add_bank():
    name = input("Enter bank name: ")
    branch_name = input("Enter branch name: ")
    account_no = int(input("Enter account number: "))
    age = int(input("Enter age: "))
    if age >= 18:
        print("Welcome To Our Bank")
    else:
        print("Below 18 is not allow")
        show_main_menu()
    mobile_no = int(input("Enter mobile number: "))
    salary = int(input("Enter your salary: "))

    bank = Bank(name, branch_name, account_no, age, mobile_no, salary)
    bank_object.append(bank)
    print("Bank added successfully...\n\n")
    show_main_menu()


def view_bank():
    print()
    if len(bank_object) == 0:
        print("No Bank account found! Please add one")
        show_main_menu()
    else:
        for bank in bank_object:
            print("Bank name:", bank.name)
            print("Branch name:", bank.branch)
            print("Account number:", bank.account_no)
            print("Age:", bank.age)
            print("Mobile number:", bank.mobile_no)
            print("Salary:", bank.salary)
            print()
        # show_main_menu()


def remove_bank():
    view_bank()
    print()
    account_no = int(input("Enter account number: "))
    for index in range(len(bank_object)):
        if bank_object[index].account_no == account_no:
            bank_object.pop(index)
            print("Bank removed successfully!")
            show_main_menu()
    print("Bank not found! please enter valid account number")
    remove_bank()


def show_bank_menu(bank):
    print("1. My Profile")
    print("2. Apply for loan")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            bank.enquiry()

        case 2:
            if bank.age >= 25:
                principal = int(input("Enter the loan amount: "))
                annual_interest_rate = float(input("Enter the annual interest rate: "))
                loan_period = int(input("Enter the loan period (in years): "))
                bank.apply_for_loan(principal, annual_interest_rate, loan_period)
                show_bank_menu(bank)  # Add this line to return to the bank menu after applying for a loan
                bank.apply_for_loan()
            else:
                print("You are not eligible for a loan. Minimum age requirement is 25.")
                show_bank_menu(bank)

        case 3:
            show_main_menu()
        case _:
            print("Invalid choice! please try again...\n\n")
            show_bank_menu(bank)


def select_bank():
    view_bank()
    print()
    account_no = int(input("Enter account number: "))
    for index in range(len(bank_object)):
        if bank_object[index].account_no == account_no:
            select_bank_object = bank_object[index]
            print("Your selected bank details:")
            print("Bank name:", select_bank_object.name)
            print("Branch name:", select_bank_object.branch)
            print("Account number:", select_bank_object.account_no)
            print("Age:", select_bank_object.age)
            print("Mobile number:", select_bank_object.mobile_no)
            print("Salary:", select_bank_object.salary)
            print()
            show_bank_menu(select_bank_object)
        else:
            print("Bank not found! please enter valid account number")
    select_bank()


def show_main_menu():
    print("1. Add Bank")
    print("2. Remove Bank")
    print("3. View Bank")
    print("4. Select Bank")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            add_bank()
        case 2:
            remove_bank()
        case 3:
            view_bank()
        case 4:
            select_bank()
        case 5:
            print("Thank you!")
            sys.exit()
        case _:
            print("Invalid choice! please try again...\n\n")
            show_main_menu()


show_main_menu()
