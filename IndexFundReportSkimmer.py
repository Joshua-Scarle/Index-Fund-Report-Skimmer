import re

def process_input(input_data):
    # (This function remains the same)
    lines = input_data.strip().split("\n")
    stock_data = []
    for line in lines:
        tokens = line.split()
        stock_name = None
        value = None
        for token in tokens:
            if re.search(r"[a-zA-Z]", token) and stock_name is None:
                stock_name = token
            elif token.endswith("%"):
                try:
                    value = float(token.strip('%')) / 100
                    break
                except ValueError:
                    print(f"Error parsing percentage value: {token}")
                    value = None
        if stock_name and value is not None:
            stock_data.append((stock_name, value))
        elif stock_name is not None and value is None:
            print(f"No percentage found for stock: {stock_name}")
        elif stock_name is None and value is not None:
            print(f"No stock name found for percentage: {value*100:.2f}%")
    return stock_data

def get_full_stock_list(prompt):
    print(prompt)
    print("Paste the stock data. Press Enter twice to finish:")
    stock_data_lines = []
    while True:
        line = input()
        if not line.strip():  # Check for empty line
            break
        stock_data_lines.append(line)
    return process_input("\n".join(stock_data_lines))  # Join lines before processing

def get_top_50(stocks):
    return sorted(stocks, key=lambda x: x[1], reverse=True)[:50]

def compare_stocks(top50_list1, list2):
    results = []
    for stock1_name, stock1_value in top50_list1:
        matched = False
        for stock2_name, stock2_value in list2:
            if stock1_name == stock2_name:
                results.append((stock1_name, stock2_value - stock1_value))
                matched = True
                break
        if not matched:
            results.append((stock1_name, "N/A"))
    return results

list1 = get_full_stock_list("Enter data for the first quarterly report:")

print("\nThe first quarterly report has been processed. Please now enter the second quarterly report.")

list2 = get_full_stock_list("Enter data for the second quarterly report:")

top50_list1 = get_top_50(list1)
comparison_results = compare_stocks(top50_list1, list2)

print("\nDifferences in the top 50 stocks between the two reports:")
for stock_name, diff in comparison_results:
    if isinstance(diff, str):
        print(f"{stock_name}: {diff}")
    else:
        print(f"{stock_name}: {diff * 100:.2f}%")
