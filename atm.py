class Atm:
    def __init__(self,cardno,pin,amount):
        self.cardno = cardno
        self.pin = pin
        self.amount = amount
    def checkbalance(self):
        print(self.amount)
    def withdrawal(self,money):
        net_amount = self.amount-money
        print(' you have withdrawn amount '+str(money)+' avaliable balance is ' +str( net_amount ))
card_num = input('please enter your card no')
pin = input ('please enter you pin')
amount = int(input('please enter amount'))
newuser = Atm(card_num,pin,amount)

print(newuser.checkbalance())
print (newuser.withdrawal(100))


