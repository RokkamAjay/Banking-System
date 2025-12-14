class BankAccount:
    def __init__(self,owner_name,balance=0):
        self.owner_name=owner_name
        self.balance=balance
        self.transcation=[]
    
    def deposite(self,amount):
        try:
            if amount <= 0:
                raise ValueError("Deposite Amount Must be Postive!")
            self.balance += amount
            self.transcation.append(f"Deposite amount: {amount}")
            print(f'The {amount} is Deposited Successfully. Balance : {self.balance}')
        
        except ValueError as e:
            print(" Error: ",e)

        except Exception as ex:
            print(ex)
    
    def withdraw(self,amount):
        try:
            if amount <= 0:
                raise ValueError("WithDraw amount must be postive!")
            
            if amount > self.balance:
                raise ValueError("Insufficient Funds!")
            
            self.balance -= amount
            self.transcation.append(f"Withdraw amount: {amount}")
            print(f"{amount} WithDraw Succesfully. Balance : {self.balance}")

        except ValueError as e:
            print("Error:",e)

        except Exception as ex:
            print(ex)

    def get_balance(self):
        return self.balance
    
    def show_transcation(self):
        print("\n Transcation History!")
        if not self.transcation:
            print("No Transcation At!")
        
        else:
            for t in self.transcation:
                print("-",t)




account =BankAccount("Ajay",50000)
account.deposite(10000)
account.withdraw(7000)
account.withdraw(60000)
account.deposite(-500)

print(f'Current Balance: {account.get_balance()}')
account.show_transcation()
