import json
import pandas as pd

class CalculateReturn:
    def __init__(self, buy_price, sell_price, quantity):
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity
        self.return_val = self.calc_return()
        self.profit = self.return_val
        self.adition_expenses = 0

    def calc_return(self):
        return (self.sell_price - self.buy_price) * self.quantity
    
    def finances(self, jsonify=False):
        data = {
            'buy_price_unit': self.buy_price,
            'sell_price_unit': self.sell_price,
            'buy_price_total': self.buy_price * self.quantity,
            'sell_price_total': self.sell_price * quantity,
            'adition_expenses': self.adition_expenses,
            'return': self.return_val,
            'profit': self.profit
        }
        if jsonify:
            return json.dumps(data, indent=4)
        return data

    def additional_expenses(self, *args, **kwargs):
        total = 0
        for index, expense in enumerate(args, start=1):
            total += expense
            self.__dict__[f'additional_expense_{index}'] = expense

        for key, val in kwargs.items():
            total += val
            self.__dict__[key] = val
            
        self.adition_expenses = total
        self.profit = self.return_val - total
    
# buy_price = 60
# sell_price = 120
# quantity = 4000
# calc = CalculateReturn(buy_price, sell_price, quantity)
# print(calc.return_val)
# print(calc.finances(jsonify=True))
# calc.additional_expenses(
#     transportation=30000,
#     food_during_buying=2000,
#     food_during_selling=7000,
#     accomodation_during_selling=5000,
#     accomodation_during_buying=10000,
#     authorities=20000
# )
# # calc.additional_expenses(30000, 2000, 5000, 5000)
# print(calc.return_val)
# print(calc.finances(jsonify=True))
# print(calc.__dict__)


class Item:
    def __init__(self, buy_price, sell_price, quantity):
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity

    def total_sell_price(self):
        return self.sell_price * self.quantity
    
    def total_buy_price(self):
        return self.buy_price * self.quantity
    
    def get_return(self):
        return (self.sell_price - self.buy_price) * self.quantity
    
    def __del__(self):
        print('Here')
    
class ReturnCalculation:
    def __init__(self, transportation, food, items=[]):
        self.items = []
        self.transportation = transportation
        self.food = food
        for item in items:
            if isinstance(item, Item):
                self.items.append(item)
        self.total_return = self.calculate_return()
        self.total_buy = self.calculate_total_cost('buy')
        self.total_sell = self.calculate_total_cost('sell')

    def calculate_total_cost(self, cost_type):
        total = 0
        for item in self.items:
            if cost_type == 'buy':
                total += item.total_buy_price()
            elif cost_type == 'sell':
                total += item.total_sell_price()
        return total

    def calculate_return(self):
        total = 0
        for item in self.items:
            total += item.get_return()
        return total
    
    def profit(self):
        return self.calculate_return() - (self.transportation + self.food)
    
    def finance(self, jsonify=False):
        data = {
            'total_buy': self.total_buy,
            'total_sell': self.total_sell,
            'total_return': self.total_return,
            'profit': self.profit()
        }
        if jsonify:
            return json.dumps(data, indent=4)
        return data

# women_trourers = Item(buy_price=350, sell_price=950, quantity=20)
# women_sandals = Item(buy_price=250, sell_price=650, quantity=20)
# men_troursers = Item(buy_price=530, sell_price=950, quantity=20)
# men_sandals = Item(buy_price=250, sell_price=650, quantity=20)
# items = [women_sandals, women_trourers, men_sandals, men_troursers]
# return_calc = ReturnCalculation(transportation=7500, food=1500, items=items)
# print(return_calc.finance(jsonify=False))
# del women_sandals
# print(return_calc.finance(jsonify=False))


def format_decimal(val):
    return round(val, 2)

class FishSelling:
    def __init__(self, budget, buy_price_by_kg, sell_price_by_kg, transp, handler):
        self.budget = budget
        self.buy_price_by_kg = buy_price_by_kg
        self.sell_price_by_kg = sell_price_by_kg
        self.transp = transp
        self.handler = handler
        self.budget -= (self.transp + self.handler)
        self.quantity = self.budget / self.buy_price_by_kg

    def calculate_return(self, n_times):
        data = []
        for _ in range(n_times):
            return_val = (self.sell_price_by_kg - self.buy_price_by_kg) * self.quantity
            profit = return_val # - (self.transp + self.handler)
            row = {
                'budget': format_decimal(self.budget),
                'buy_price': format_decimal(self.buy_price_by_kg), 
                'sell_price': format_decimal(self.sell_price_by_kg), 
                'quantity': format_decimal(self.quantity),
                'transportation': format_decimal(self.transp),
                'handler': self.handler,
                'return': format_decimal(return_val),
                'profit': format_decimal(profit)
            }
            data.append(row)
        df = pd.DataFrame(data)
        # print(df)
        # print(df[['budget', 'return', 'profit']].sum(axis=0).T)
        # print(df['profit'].sum(axis=0))
        return df
        
    def calculate_return2(self, n_times):
        return_val = (self.sell_price_by_kg - self.buy_price_by_kg) * self.quantity
        profit = return_val # - (self.transp + self.handler)
        row = {
            'budget': format_decimal(self.budget),
            'buy_price': format_decimal(self.buy_price_by_kg), 
            'sell_price': format_decimal(self.sell_price_by_kg), 
            'quantity': format_decimal(self.quantity),
            'transportation': format_decimal(self.transp),
            'handler': self.handler,
            'return': format_decimal(return_val),
            'profit': format_decimal(profit)
        }
        data = [row]
        for _ in range(n_times-1):
            self.budget += profit
            self.quantity = self.budget / self.buy_price_by_kg
            self.transp *= 2
            self.handler *= 1.3
            return_val = (self.sell_price_by_kg - self.buy_price_by_kg) * self.quantity
            profit = return_val # - (self.transp + self.handler)
            row = {
                'budget': format_decimal(self.budget),
                'buy_price': format_decimal(self.buy_price_by_kg), 
                'sell_price': format_decimal(self.sell_price_by_kg), 
                'quantity': format_decimal(self.quantity),
                'transportation': format_decimal(self.transp),
                'handler': self.handler,
                'return': format_decimal(return_val),
                'profit': format_decimal(profit)
            }
            data.append(row)
        df = pd.DataFrame(data)
        print(df[['budget', 'return', 'profit']])
        

# calc = FishSelling(budget=30000, buy_price_by_kg=150, sell_price_by_kg=260, transp=1200, handler=2000)
# df = calc.calculate_return(4)
# print(df)
# calc2 = FishSelling(budget=30000, buy_price_by_kg=150, sell_price_by_kg=260, transp=1200, handler=2000)
# calc2.calculate_return2(4)


def calculate(buy, sell, qty, transportation, food=0, helpers=2000):
    return {
        'buy': buy,
        'sell': sell,
        'quantity': qty,
        'food': food,
        'helpers': helpers,
        'transportation': transportation,
        'buy_total': buy * qty,
        'sell_total': sell * qty,
        'return_val': ((sell - buy) * qty) - (transportation + food + helpers)
    }

# buy, sell, qty, transportation, food, helpers = 200, 390, 200, 3000, 700, 1000
# data = calculate(buy, sell, qty, transportation, food, helpers)
# return_value = data['return_val']
# for index in range(1, 11):
#     print(f'return #{index} = {return_value}')
#     data = calculate(buy, sell, qty, transportation, food, helpers)
#     return_value += data['return_val']

# print(json.dumps(calculate(), indent=4))
# print(json.dumps(calculate(120, 300, 100, 3000, helpers=500), indent=4))

land_price = 250000
construction_cost = 600000
total = 0
print(6 * 15000 * 12 * 3)
print(35 * 2000 * 6)