class Account():
    
    #default value for balance is zero
    def __init__(self,owner,balance=0):
        
        self.owner = owner
        self.balance = balance
        print("Account owner: {}".format(self.owner))
        print("Account balance: {}".format(self.balance))
        
    def deposit(self,dep):
        
        self.balance = self.balance + dep
        print("Deposit accepted")
        
    def withdraw(self,withd):
        
        #only if current balance is greater than or equal to withdraw 
        if self.balance >= withd:
            
            self.balance = self.balance - withd
            print("Withdrawal accepted")
            return self.balance
        
        else:
            
            print("Funds Unavailable")
