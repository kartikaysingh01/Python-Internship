stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

n = int(input("Enter number of stocks: "))

for i in range(n):

    stock = input("Enter stock name: ").upper()

    qty = int(input("Enter quantity: "))

    if stock in stocks:

        investment = stocks[stock] * qty

        total_investment += investment

        print("Investment in", stock, "=", investment)

    else:

        print("Stock not found")

print("\nTotal Investment Value =", total_investment)

f = open("portfolio.txt", "w")

f.write("Total Investment Value = " + str(total_investment))

f.close()

print("Result saved in portfolio.txt")
