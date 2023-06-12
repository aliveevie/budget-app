class Category:
    
    def __init__(self, description):
        self.description = description
        self.ledger = list()
        self.initial_balance = 0.0
        
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        
    def get_balance(self):
        total = self.initial_balance
        for transaction in self.ledger:
            total += transaction['amount']
        return total
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.description}")
            category.deposit(amount, f"Transfer from {self.description}")
            return True
        else:
            return False
        
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"{self.description:*^30}\n"
        items = ""
        total = 0
        
        for transaction in self.ledger:
            items += f"{transaction['description'][:23]:23} {transaction['amount']:7.2f}\n"
            total += transaction['amount']
        output = f"{title}{items}Total: {total}"
        return output
    
 
def create_spend_chart(categories):
    # Calculate the total withdrawals for all categories
    total_withdrawals = sum(category.get_balance() for category in categories)
    
    withdrawal_percentages = [category.get_balance() / total_withdrawals * 100 for category in categories]
    
    # Build the chart 
    chart = 'Percentage spent by category\n'
    for i in range(100,  -10, -10):
        chart += str(i).rjust(3) + "| "
        
        for percentage in withdrawal_percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
            
        chart += "\n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Find the maximum length of category names:
    max_length = max(len(category.description) for category in categories)
   
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.description):
                chart += category.description[i] + "  "
            else:
                chart += "   "

        if i != max_length - 1:
            chart += "\n"
   
    return chart
