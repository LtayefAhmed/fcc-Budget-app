class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]

    def __str__(self):
        title=f"{self.name:*^30}\n"
        items=""
        for item in self.ledger:
            description=item['description'][:23]
            amount=item['amount']
            items+=f"{description:<23}{amount:>7.2f}\n"
        total=self.get_balance()
        total_line=f"Total: {total}"
        return title+items+total_line

    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})
        return self.ledger

    def withdraw(self, amount,description=''):
        
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        funds=0
        for i in self.ledger:
            funds+=i['amount']
        return funds

    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    
    def check_funds(self,amount):
        balance=self.get_balance()
        return  amount <= balance 

    


def create_spend_chart(categories):
    #calcul des depenses
    spent_amounts=[]
    for category in categories:
        spent=0
        for item in category.ledger:
            if item['amount']<0:
                spent+=abs(item['amount'])
        spent_amounts.append(spent)
    
    total_spent= sum(spent_amounts)
    percentages=[]
   #calcul des pourcentages
    for amount in spent_amounts:
        percentage=(amount/total_spent)*100
        percentages.append(int(percentage//10)*10)
    
    chart = "Percentage spent by category\n"

    for i in range (100,-1,-10):
        chart+=str(i).rjust(3) + '| '
        for percent in percentages:
            if percent >= i :
                chart += 'o '
            else:
                chart+= "   "
        
        chart +='\n'
    

    chart+= "    " + "-"*(len(categories)*3+1) + "\n"


    max_len=0
    for category in categories:
        if len(category.name) > max_len:
            max_len = len(category.name)

    
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] +"  "
            
            else:
                chart += "   "

        if i < max_len-1:
            chart += "\n"
    
    return chart


