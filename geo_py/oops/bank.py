class bank:
    acc_no:int
    bank_name:str
    branch:str
    personal_name:str
    ifsc_code:int
    balance:int

    def create(self,acc_no,bank_name,branch,personalname,ifsc_code,balance):
        self.acc_no=acc_no
        self.bank_name=bank_name
        self.branch=branch
        self.personal_name=personalname
        self.ifsc_code=ifsc_code
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited with amount {amount} aval balance {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficent balance transaction failed")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} has been debited with amount {amount} aval balance {self.balance}") 

    def get_balance(self):
        print(f"your avaliable balance is{self.balance}")


obj=bank()
obj.create(2211334,"sbi","kottarakara","sabin","sbi2311",36000)

obj.deposit(12000)
obj.withdraw(100000)