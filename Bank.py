class Bank:
    def __init__(self):
        self.acc_no=0
        self.bal=0
        print(self.bal)

    def addbank(self):
        self.acc_no=int(input("Enter account number:"))
    def deposit(self):
        amt=int(input("Enter amount:"))
        self.bal=self.bal+amt
    def withdraw(self):
        amt=int(input("Enter amount:"))
        self.bal=self.bal-amt
        print("amount withdrawn")
