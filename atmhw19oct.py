# Create constructor and objects for ATM class

class ATM:
    def __init__(self, pin, balance):
        print("ATM constructor is running")
        self.pin = pin
        self.balance = balance

atm1 = ATM(1234, 10000)
atm2 = ATM(5678, 7500)

print(atm1.balance)
print(atm2.balance)