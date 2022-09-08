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
    self.ledger.append({
      'amount': -amount, 
      'description': description
    })
    

  def get_balance(self, amount) :
    self.amount = amount

def create_spend_chart(categories):
  return