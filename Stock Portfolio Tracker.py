def portfolio_tracker():
    # 1. Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 135,
        "AMZN": 145
    }
    
    total_investment = 0
    print("Available stocks:", list(stock_prices.keys()))
    print("Type 'done' to finish adding stocks.\n")

    # 2. User Input Loop
    while True:
        stock_name = input("Enter Stock Name (e.g., AAPL): ").upper()
        
        if stock_name == "DONE":
            break
            
        if stock_name in stock_prices:
            try:
                quantity = int(input(f"Enter quantity for {stock_name}: "))
                cost = stock_prices[stock_name] * quantity
                total_investment += cost
                print(f"Added {quantity} {stock_name} shares. Current Total: ${total_investment}")
            except ValueError:
                print("Invalid number entered for quantity.")
        else:
            print("Stock not found in our simplified database.")

    # 3. Output result
    print("-" * 30)
    print(f"Total Portfolio Value: ${total_investment}")
    print("-" * 30)

if __name__ == "__main__":
    portfolio_tracker()