class Category:
  def __init__(self, name):
    self.name = name
    self.total = 0.0
    self.ledger = list()

  def deposit(self, amount, description=''):
    self.total += amount
    self.description = description 
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ''):
    check_if_has_funds = self.check_funds(amount)
     
    if check_if_has_funds == True: 
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  
  def get_balance(self):
    return self.total
  
  def transfer(self, amount, destination):
    check_if_can_transf = self.check_funds(amount)
    
    if check_if_can_transf == True:
      self.withdraw(amount, f"Transfer to {destination.name}")
      destination.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False
  def check_funds(self, amount):
    if  amount > self.total:
      return False #transferation invalid
    else:
      return True #transferation valid 
  
  def __str__(self):
    output = self.name.center(30, "*") + "\n"
    total = 0
    for i in self.ledger:
      output += f"{i['description'][0:23]:23}{i['amount']:>7.2f}\n"
      total += i['amount']
    output += f'Total: {total}'
    return output
    
def create_spend_chart(categories):
  category_names = [] # essa lista com a de baixo terá uma correlação de indices
  spent = [] # cada elemento da lista é a soma dos withdraws de cada categoria
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']  #soma dos withdraws de uma categoria 
    spent.append(round(total, 2)) # adicionando o total de withdraws da categoria na lista
    category_names.append(category.name) 

  for category_amount in spent:
    spent_percentages.append(round(category_amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -1 , -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0
  
  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length - 1:
      graph += "\n     "

  return(graph)
