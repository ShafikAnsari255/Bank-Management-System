import json
class BankAccount:
    def __init__(self, name, balence, pin, account_number):
        self.name = name
        self.balence = balence
        self.pin = pin
        self.account_number = account_number
        self.history = []

    def check_pin(self, entered_pin):
        if entered_pin == self.pin:
            return True
        else:
            return False    

    def account_details(self):
        print()
        print("------Welcome to punjab national bank ------")
        print()

        print(f"Account Holder Name: ",self.name)
        print(f"Account Number: ", {self.account_number})
        print(f"Current balence: ",self.balence)        

    def deposit(self, amount):
        self.balence += amount
        self.history.append(f"Deposit {amount}")
        print()
        print(f"Money Deposited Successfully: {amount}")

    def withdraw(self, amount):
        if amount <= self.balence:
            self.balence -= amount
            self.history.append(f"Withdraw {amount}")
            print()
            print(f"Money Withdraw Successfully: {amount}")
            print(f"Current Balence:  {self.balence}")
        else:
            print()
            print("insufficient balence")

    def transfer_money(self, receiver, amount):
        if amount <= self.balence:
            self.balence -= amount
            receiver.balence += amount
            self.history.append(f"Transfered {amount} to {receiver.name}")
            receiver.history.append(f"Received {amount} from {self.name}")
            print()
            print(f"Money Transfer Successfully to {receiver.name}")
            print(f"Your Current Balence: {self.balence}")
            print(f"{receiver.name} New Balence: {receiver.balence}")

        else:
            print()
            print("Insufficient balence")    

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN Changed Successfully")
        else:
            print("Wrong Old PIN")     

    def mini_statement(self):
        print()
        print("------ MINI STATEMENT ------")
        print()
        for transaction in self.history[-3:]:
            print(transaction)                    

    def check_balence(self):
        print(f"Current Balence: {self.balence}")

    def show_history(self):
        print()
        print("------ TRANSACTION HISTORY ------")
        print()
        for transaction in self.history:
            print(transaction)

    def to_dict(self):
        return{
            "name": self.name,
            "balence": self.balence,
            "pin": self.pin,
            "account_number": self.account_number,
            "history": self.history
        }        

acc1 = BankAccount("Shafik Ansari", 5000, 1234, "40271XXXX")
acc2 = BankAccount("Zaved Ansari ", 40000, 5678, "40272XXXX")
acc3 = BankAccount("Shakil Ansari", 50000, 4321, "40273XXXX")
acc4 = BankAccount("Emamuddin Ansari", 45000, 8765, "40274XXXX")

def save_account(account):
    data = []
    for acc in account:
        data.append(acc.to_dict())
    with open("account.json","w") as file:
        json.dump(data, file, indent=4) 

account = []
account.append(acc1)
account.append(acc2)
account.append(acc3)
account.append(acc4)
print("="*40)
print("    PUNJAB NATIONAL BANK")           
print("="*40)
print()
pin = int(input("Enter PIN: "))
found = False
for acc in account:
    if acc.check_pin(pin):
        found = True
        print()
        print("Login Successful")

        acc.account_details()
        print()
        print("1. Deposite Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            deposit_amount = int(input("Enter Deposite Amount: "))
            acc.deposit(deposit_amount)
            save_account(account)
            acc.check_balence()
            acc.show_history()

        elif choice == 2:
            withdraw_amount = int(input("Enter Withdraw Amount: "))
            acc.withdraw(withdraw_amount)
            save_account(account)
            
        elif choice == 3:
            receiver_acc = input("Enter Receiver Account Number: ")
            transfer_amount = int(input("Enter Transfer Amount: "))

            receiver_found = False
            for user in account:
                if user.account_number == receiver_acc:
                    receiver_found = True
                    acc.transfer_money(user, transfer_amount)
                    save_account(account)
                    acc.check_balence()
                    acc.show_history()
                    acc.mini_statement()
            if receiver_found == False:
                print()
                print("Wrong Account Number")  

        elif choice == 4:
            old_pin = int(input("Enter Old PIN: "))
            new_pin = int(input("Enter New PIN: "))
            acc.change_pin(old_pin, new_pin)
            save_account(account)

        elif choice == 5:
            acc.mini_statement()

        else:
            print("Invalid Choice")    
        
if found == False:        
    print()
    print("Wrong PIN")