class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        total = 0
        for item in self.ledger:
          items += f'{item["description"][0:23]:23}' + f'{item["amount"]:>7.2f}' + '\n'
          
          total += item['amount']
        output = title + items + 'Total: ' + str(total)
        return output

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        return False

    def get_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item['amount']
        return total_cash

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}.')
            category.deposit(amount, f'Transfer from {self.name}.')
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False
      
    def get_withdrawals(self):
        total = 0
        for item in self.ledger :
          if item['amount'] < 0 :
            total += item['amount']
        return total

def create_spend_chart(categories):
    return
