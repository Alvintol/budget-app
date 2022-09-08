class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        total = 0
        for item in self.ledger:
            items += f'{item["description"][0:23]:23}' + \
                f'{item["amount"]:>7.2f}' + '\n'

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
        for item in self.ledger:
            if item['amount'] < 0:
                total += item['amount']
        return total


def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier


def get_totals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())
    rounded = list(map(lambda item: truncate(item/total), breakdown))
    return rounded


def create_spend_chart(categories):
    output = 'Percentage spent by category\n'
    yAxis = 100
    totals = get_totals(categories)
    while yAxis >= 0:
        categorySpaces = ' '
        for total in totals:
            if total * 100 >= yAxis:
                categorySpaces += 'o '
            else:
                categorySpaces += '  '
        output += str(yAxis).rjust(3) + '|' + categorySpaces + ('\n')
    bar = '-' + '---' * len(categories)
    names = []
    xAxis = ''
    for category in categories:
        names.append(category.name)
    
    maxAxis = max(names, key = len)
    
    for char in range(len(maxAxis)):
        nameStr = '     '
        for name in names:
            nameStr += '  '
        else:
            nameStr += name[char] + ' '
    
        if char != len(maxAxis) -1:
            nameStr += '/n'
        
        xAxis += nameStr
    
    output += bar.rjust(len(bar) + 4) + '/n' + xAxis
    return output
