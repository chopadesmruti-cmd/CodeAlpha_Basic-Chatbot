# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 300,
    "AMZN": 3500
}

def stock_portfolio():
    portfolio = {}
    total_investment = 0
    
    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not found! Please choose from available stocks.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        # Store in portfolio
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += stock_prices[stock] * quantity
    
    print("\n📊 Your Portfolio Summary:")
    for stock, qty in portfolio.items():
        print(f"{stock} ({qty} shares) = ${stock_prices[stock] * qty}")
    print(f"\n💰 Total Investment Value = ${total_investment}")
    
    # Optional: Save to file
    save = input("\nDo you want to save portfolio to file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock} ({qty} shares) = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value = ${total_investment}\n")
        print("✅ Portfolio saved to portfolio.txt")

# Run the tracker
stock_portfolio()