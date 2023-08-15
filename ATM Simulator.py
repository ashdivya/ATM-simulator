class Bank:
    bal=90000
    def login(self,pin):
        if pin==9090:
            return True
        else:
            return False
    def credit(self,amt):
        self.bal+=amt
    def debit(self,amt):
        self.bal-=amt
    def show(self):
        print("current balance is "+str(self.bal))
obj=Bank()
flag=False
for i in range(1,4):
    if obj.login(int(input("enter pin code"))):
        flag=True
        break
if flag:
    while True:
        print("1.credit\n2.debit\n3.balance\n4.exit")
        print("enter option to proceed")
        option=input()
        if option=="1":
            obj.credit(int(input("enter amount for credit")))
            print("after credit total amount is "+str(obj.bal))
        elif option=="2":
            amt=int(input("enter amount for debit"))
            if amt<obj.bal:
                obj.debit(amt)
                print("after debit total amount is "+str(obj.bal))
            else:
                print("insufficient balance")
        elif option=="3":
            obj.show()
        elif option=="4":
            exit()
        else:
            print("you entered wrong option.please enter correct option")
else:
    print("You enter wrong pin. please try again!")
            
