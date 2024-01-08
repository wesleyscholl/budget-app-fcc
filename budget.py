class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.category}")
            destination.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{'*' * ((30 - len(self.category)) // 2)}{self.category}{'*' * ((30 - len(self.category)) // 2)}"
        lines = [title]

        total = 0
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            lines.append(f"{description:<23}{amount:>7}")

            total += item['amount']

        lines.append(f"Total: {total:.2f}")
        return '\n'.join(lines)


def create_spend_chart(categories):
  category_names = [category.category for category in categories]
  spent = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
  total_spent = sum(spent)
  percentages = [(amount / total_spent * 100) // 10 * 10 for amount in spent]
  graph = "Percentage spent by category\n"
  for i in range(100, -10, -10):
      graph += f"{i:>3}| {''.join('o  ' if percent >= i else '   ' for percent in percentages)}\n"
  graph += "    " + "-" * (len(categories) * 3 + 1) + "\n"
  max_len = max(len(name) for name in category_names)
  for i in range(max_len):
      graph += "     "
      for name in category_names:
          if i < len(name):
              graph += f"{name[i]}  "
          else:
              graph += "   "
      if i < max_len - 1:
          graph += "\n"
  return graph
