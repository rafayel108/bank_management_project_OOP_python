
x=1000
class Account:
    accounts=[]
    loan_amount=0
    bankrupt=0
    
    def __init__(self,name,email,address,type):
        self.name=name
        self.email=email
        self.address=address
        self.balance = 0
        self.type=type
        global x
        self.account_number=x+1
        x=self.account_number
        self.loan_approval=0
        self.transaction=[]
        self.loan=0
        
        Account.accounts.append(self)
    
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            self.transaction.append(f'Money {amount} deposited to account')
            print(f"\n--> Deposited {amount} to the account number {self.account_number}.\n    New balance: ${self.balance}")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction.append(f'Money {amount} withdrown from account')
            print(f"\n--> Withdrew ${amount}.\n    New balance: ${self.balance}")
        else:
            print("\nWithdrawal amount exceeded")

    def balances(self):
        return self.balance
        

    def transaction_history(self):
        print(self.transaction)    
    
    def loan_req(self,amount):
        if self.loan==0 or self.loan==1:
            print(f'\nAccount {self.account_number} is eligible for loan {amount}. Please contact at Bank\'s main branch.')
            self.loan+=1
            Account.loan_amount+=amount
            self.transaction.append(f'Loan Taken {amount}')
        else:
            print(f'\nLoan limit of Account {self.account_number} is exceed ')

    def transfer_receive(self,amount,tt,ff):
        self.balance+=amount
        self.transaction.append(f'Account {tt} Amount {amount} received from {ff}')
        

    def transfer_from(self,amount,t,f):
        self.balance-=amount
        self.transaction.append(f'Amount {amount} is transfered to {t}')
        print(f'\nTransfer to account {t} from account {f} is completed. Your current balance is {self.balance}')

        
class AdminAccount(Account):
    def __init__(self,name,email,address):
        
        super().__init__(name,email,address,'Admin')
        print(f'\nAdmin Account opened with the name: {self.name} and Account number: {self.account_number}')




class SavingsAccount(Account):
    def __init__(self,name,email,address):
        
        super().__init__(name,email,address,'Savings')
        print(f'\nSavings Account opened with the name: {self.name} and Account number: {self.account_number}')
        
    


class CurrentAccount(Account):
    def __init__(self,name,email,address):
        super().__init__(name,email,address,"Current")
        print(f'\nCurrent Account opened with the name: {self.name} and account number: {self.account_number}')




while True:
    l=input(f'\nType \'U\'  for User Login\nType \'A\' for Admin Login\nType \'E\' for Exit Banking\n------------------------\nType here->')  
    if l=='U':
        while(True):
            print('\n1.Open Account\n2.Deposit Money\n3.Withdraw Money\n4.Check Balance\n5.Transaction History\n6.Loan Request\n7.Transfer Money\n8.Logout User\n')
            j=input()
            if j=='8':
                print('\nUser logout successful.')
                break
            elif j=='1':
                k=input(f'\nFor Savings Account press \'S\'\nFor Current Account press\'C\'\n')
                if k=='S':
                    n=input(f'Enter Name: ')
                    e=input(f'Enter email: ')
                    a=input(f'Enter Address: ') 
                    SavingsAccount(n,e,a)
                
                elif k=='C':
                    p=input(f'Enter Name: ')
                    o=input(f'Enter email: ')
                    u=input(f'Enter Address: ')
                    CurrentAccount(p,o,u)
                
                else:
                    print('You have typed a wrong key')
            elif j=='2':
                d1=int(input(f'Enter Account Number: '))
                d2=int(input('Enter the ammount to deposit: '))
                d3=0
                d4=None
                for acc in Account.accounts:
                    if acc.account_number==d1:
                        d3=1
                        d4=acc
                if d3==1:
                    d4.deposit(d2)
                else:
                    print('\nAccount does not exist')



            elif j=='3':
                if Account.bankrupt==0:

                    w1=int(input(f'Enter Account Number: '))
                    w2=int(input('Enter the ammount to withdraw: '))

                    w3=0
                    w4=None
                    for acc in Account.accounts:
                        if acc.account_number==w1:
                            w3=1
                            w4=acc
                    if w3==1:
                        w4.withdraw(w2)
                    else:
                        print('\nAccount does not exist')
                else:
                    print('\nSorry! Bank is bankrupt.Withdraw can not possible due to bankruptcy.')        


            elif j=='4':
                b=int(input(f'Enter Account Number: '))
                b1=0
                b2=None
                for acc in Account.accounts:
                    if acc.account_number==b:
                        b2=acc
                        b1=1
               
                if b1==1:
                    z=b2.balances()
                    print(f'\nAccount {b} has balance {z}')
                else:
                    print('\nAccount does not exist.')    

            elif j=='5':
                t=int(input(f'Enter Account Number: '))
                t1=0
                t2=None
                for acc in Account.accounts:
                    if acc.account_number==t:
                        t1=1
                        t2=acc

                if t1==1:
                    print('\n')
                    t2.transaction_history()
                else:
                    print('\nAccount does not exist.')   

            elif j=='6':
                if Account.bankrupt==0:
                    l=int(input(f'Enter Account Number: '))
                    l1=0
                    l2=None
                    for acc in Account.accounts:
                        if acc.account_number==l:
                            l1=1
                            l2=acc
                            l3=acc.loan_approval

                    if l1==1:
                        if l3==0:
                            am=int(input(f'Enter Loan Amount: '))
                            l2.loan_req(am)
                        else:
                            print('\nYour loan procedure is turned off by Admin.')    

                    else:
                        print('\nAccount does not exist.') 
                else:
                    print('\nSorry! Bank is bankrupt. Loan request can not possible due to bankruptcy.')    
       

            elif j=='7':
                if Account.bankrupt==0:

                    f1=int(input(f'Enter Your Account Number: '))
                    f11=0
                    f111=None
                    p=None
                    f=None
                    for acc in Account.accounts:
                        if acc.account_number==f1:
                                p=acc.balances()
                                f=int(input(f'You have balance {p}. Enter amount to transfer: '))
                                f11=1
                                f111=acc
                    if f11==1:
                            if f<= p and f>0:
                                    f2=int(input(f'Enter Account Number to send money: '))
                                    f22=0
                                    f222=None
                                    for ac in Account.accounts:
                                        if ac.account_number==f2:
                                            f22=1
                                            f222=ac
                                    
                                    if f22==1:
                                        f222.transfer_receive(f,f2,f1) 
                                        f111.transfer_from(f,f2,f1)
                                    else:
                                        print(f'\nAccount number {f2} did not matched.')  

                            
                            else:
                                print(f'\nWithdrawal amount exceeded.')
               
                else:
                    print('\nSorry! Bank is bankrupt. Transfer can not possible due to bankruptcy.')    

            
            
            else:
                print('\nYou have entered invalid key.')        
                             
    elif l=='A':
        while True:
            print('\n1.Open Account\n2.Delete account\n3.See Account List\n4.Check Total Balance\n5.Total Loan of the Bank\n6.Loan Reques off\n7.Declare Bankrupt\n8.Logout Admin\n')
            a=input()
            if a=='8':
                print('\nAdmin logout successful.\n')
                break
            elif a=='4':
                total=0
                for acc in Account.accounts:
                    t=acc.balances()
                    total+=t
                print(f'\nTotal Balance of the bank is {total}.')
            elif a=='1':
                print('\nYou are trying to open an Admin Account.Please enter the following things.\n')
                
                n=input(f'Enter Name: ')
                e=input(f'Enter email: ')
                a=input(f'Enter Address: ') 
                AdminAccount(n,e,a)

            elif a=='2':
                d2=int(input(f'Enter Your Account Number to delete: '))
            
                d3=0
                d4=None
                for acc in Account.accounts:
                    if acc.account_number==d2:
                        d3=1
                        d4=acc
                if d3==1:
                    print(f'\nAccount {d2} is deleted.')
                    Account.accounts.remove(d4)
                else:
                    print('\nAccount number did not found.')

                
            elif a=='3':
                print('\nAccounts of the Bank are given below.\n')  
                for acc in Account.accounts:
                    print(f'Account Number-> {acc.account_number}.    Account holder is \'{acc.name}\'.   Account type-> {acc.type}\n')

            elif a=='5':
                print(f'\nTotal loan of the Bank is {Account.loan_amount}')

            elif a=='6':
                ll=int(input(f'Enter Account Number to Turn off loan approval: '))
                d3=0
                d4=None
                for acc in Account.accounts:
                    if acc.account_number==ll:
                        d3=1
                        d4=acc
                if d3==1:
                    print(f'\nLoan approval of account {d4.account_number} is turned off.')
                    d4.loan_approval=1
                else:
                    print('\nAccount number did not found.')
            elif a=='7':
                print('\nThe bank is bankrupt declared. All banking will ramain shut untill next update. ')
                Account.bankrupt=1
            else:
                print('\nYou have entered worng key.')    

                    

    elif l=='E':
        print('\nBanking system exited.')
        break        
    else:
        print('\nYou have typed wrong key.')
        




