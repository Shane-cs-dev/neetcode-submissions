class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_account = 0
    total_balance = 0
    
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_account += 1
        BankAccount.total_balance += balance
    
    def PRINT(self) -> None:
        print(f"{self.name}'s balance: ${self.balance}")
    

# TODO: Create two accounts
Alice = BankAccount("Alice", 1000)
Bob = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
Alice.PRINT()
Bob.PRINT()
print(f"Total Accounts: ${BankAccount.total_account}")
print(f"Total Balance: ${BankAccount.total_balance}")


