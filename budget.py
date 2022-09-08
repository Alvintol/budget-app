class Category:
  def __init__(self, name) :
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description = '') :
    self.amount = amount
    self.description = description
    
  


def create_spend_chart(categories):
  return