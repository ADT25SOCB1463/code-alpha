# CodeAlpha Task 2: Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

total_investment = 0

for stock, price in stocks.items():
    quantity = int(input("Enter quantity of " + stock + ": "))
    investment = price * quantity
    total_investment += investment
    print(stock, "Investment:", investment)

print("Total Investment:", total_investment)
