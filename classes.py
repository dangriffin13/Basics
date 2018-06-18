

def Account(self, number, user, balance=0):
    def __init__(self, number, user, balance):
        self.account_number = number
        self.owner = user
        self.balance = balance

    def deposit(self, transaction):
        self.balance += transaction
        return transaction, self.balance

    def withdrawal(self, transaction):
        if transaction > self.balance:
            raise RunTimeError('Insufficient funds.')
        self.balance -= transaction
        return transaction, self.balance

    def view_balance(self):
        return self.balance

    