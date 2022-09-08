class Category:
  def __init__(self, name) :
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description = '') :
    self.ledger.append({
      'amount': amount, 
      'description': description
    })
    
  def withdraw(self, amount, description = '') :
    if self.check_funds(amount) : 
      self.ledger.append({
        'amount': -amount, 
        'description': description
      })
      return True
    return False

  def get_balance(self) :
    total_cash = 0
    for item in self.ledger :
      total_cash += item['amount']
    return total_cash  

def create_spend_chart(categories):
  return