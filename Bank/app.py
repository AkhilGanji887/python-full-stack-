#user table 
users = {
    1234:{'name':"akhil","Email":'akhilganji005@gmail.com','balance':30000,'password':'1234'},
    1235:{'name':"bubby","Email":'akhilganji006@gmail.com','balance':20000,'password':'1235'}
    }

#services
def register(name:str, email:str,initialdeposit:int,password:str):
    pass

def login(account:int,password:str)->bool:
    # check account exists in users or not
    if account in users:
        if password == users[account]['password']:
            print("Login successful")
            return True
    
    
    return False
#balance functin defination
def balance(account:int)->int:
    current_balance = users[account]['balance']
    return current_balance

#withdraw function defination
def withdraw(account:int,withdrawamount:int)->str:
    curr_amount = users[account]['balance']
    # check amount
    if curr_amount >= withdrawamount:
        users[account]['balance'] -= withdrawamount
        return f"{withdrawamount} Withdraw successful and \
                current Balance is: {users[account]['balance']}"

# Deposit function defination
def Deposit(account:int,deposit_amount:int):
    users[account]['balance'] += deposit_amount
    return f"{deposit_amount} Deposit successful and \
                    current Balance is: {users[account]['balance']}" 
    return "Insufficient Balance"

#Transfer Function Defination
def transfer(sender:int,reciever:int,transferamount:int):
    if reciever in users:
        curr_amount = users[sender]['balance']
        if curr_amount >= transferamount:
            users[sender]['balance'] -= transferamount
            users[reciever]['balance'] += transferamount
            return f"{transferamount} Transfer successful and \
                    current Balance is: {users[sender]['balance']}"
        return "Insufficient Balance"
    return "Reciever account not Found"

#Ministatement Function Defination
def ministatement(account:int):
    return f"Account Number:{account} \n \
            Name:{users[account]['name']} \n \
            Email:{users[account]['Email']} \n \
            Balance:{users[account]['balance']}"

#Logout Function Defination
def logout():
    return "Thank you for using our services, have a nice day"

#main
if __name__ == "__main__":
    print("Welcome to the small scale bank")
    print("1. Register \n 2.Login")
    choice = int(input("select your choice:"))

    # calling register function
    if choice == 1:
        print("Register page under development process....")

    # calling Login Function
    elif choice == 2:
        account = int(input("Enter your account number:"))
        password = input("Enter your password:")
        login_val = login(account=account, password=password)

        while login_val:
            print("The small scale Bank Providing services")
            print("1. Balance \n 2. withdraw \n 3.Deposit \n \
            4. Transfer \n 5. Ministatement \n 6 . Logout")
            choice = int(input("Enter your choice(1-6):"))

            if choice == 1:
               # call Balance function
               current_balance = balance(account=account)
               print(f"Current Balance is: {current_balance}")

            elif choice == 2:
                amount = int(input("Enter your withdrawamount:"))
                # call withdraw function
                res = withdraw(account=account, withdrawamount=amount)
                print(res)
            
            elif choice == 3:                
                amount = int(input("Enter your Deposit amount:"))
                res = Deposit(account=account, deposit_amount=amount)
                print(res)
            elif choice == 4:
                reciever_account = int(input("Enter your Transfer amount:"))
                # call Transfer Function
                res = transfer(sender= amount,reciever=amount,transferamount=amount)
                print(res)
            elif choice == 5:
                statement = int(input("Enter your account number:"))
                #call Ministatement Function
                res = ministatement(account=account)
                print(res)
            elif choice == 6:
                # call Logout Function
                print(logout())
                exit()
            else:
                print("Invalid choice, please select a valid option")
        else:
            print("Enter the valid choice 1 or 2")

             