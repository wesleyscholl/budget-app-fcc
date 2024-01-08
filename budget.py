class Category:
  def __init__(self, category):
      self.category = category  # Initialize category name
      self.ledger = []  # Initialize an empty ledger list to track transactions
  def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})  # Add a deposit to the ledger
  def withdraw(self, amount, description=""):
      if self.check_funds(amount):  # Check if there are sufficient funds for withdrawal
          self.ledger.append({"amount": -amount, "description": description})  # Add a withdrawal to the ledger
          return True  # Return True for successful withdrawal
      return False  # Return False if insufficient funds
  def get_balance(self):
      return sum(item['amount'] for item in self.ledger)  # Calculate and return current balance
  def transfer(self, amount, category):
      if self.check_funds(amount):  # Check if there are sufficient funds for transfer
          self.withdraw(amount, f"Transfer to {category.category}")  # Add withdrawal from current category
          category.deposit(amount, f"Transfer from {self.category}")  # Add deposit to the specified category
          return True  # Return True for successful transfer
      return False  # Return False if insufficient funds
  def check_funds(self, amount):
      if amount > self.get_balance():  # Check if the amount exceeds the current balance
          return False  # Return False if insufficient funds
      return True  # Return True if there are sufficient funds
  def __str__(self):
      # Create a formatted string representation of the category object
      title = f"{self.category:*^30}\n"
      items = ''.join(f"{item['description'][:23]:23}{item['amount']:>7.2f}\n" for item in self.ledger)
      total = f"Total: {self.get_balance():.2f}"
      return title + items + total

def create_spend_chart(categories):
  # Extract category names and total spending from each category
  category_names = [category.category for category in categories]  # Extract category names
  spent = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]  # Calculate total spending
  # Calculate total spending across all categories
  total_spent = sum(spent)
  # Calculate percentages spent in each category and round down to the nearest 10
  percentages = [(amount / total_spent * 100) // 10 * 10 for amount in spent]
  # Initialize the graph with the title
  graph = "Percentage spent by category\n"
  # Create the bar chart for each percentage range from 100% to 0%
  for i in range(100, -10, -10):
      graph += f"{i:>3}| {''.join('o  ' if percent >= i else '   ' for percent in percentages)}\n"
  # Add a line separator after the bars
  graph += "    " + "-" * (len(categories) * 3 + 1) + "\n"
  # Find the maximum length of category names to align the labels correctly
  max_len = max(len(name) for name in category_names)
  # Create the chart showing the category names below the bars
  for i in range(max_len):
      graph += "     "
      for name in category_names:
          if i < len(name):
              graph += f"{name[i]}  "  # Add the characters of category names vertically aligned
          else:
              graph += "   "  # Add spaces if the category name is shorter
      if i < max_len - 1:
          graph += "\n"  # Add a new line except for the last iteration
  return graph
