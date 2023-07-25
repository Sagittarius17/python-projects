# import pandas as pd

# # Create an empty DataFrame to store income and expenses
# df = pd.DataFrame(columns=['Type', 'Amount', 'Date'])

# # Define a function to add income or expenses to the DataFrame
# def add_transaction(transaction_type, amount, date):
#     global df
#     df = df.append({'Type': transaction_type, 'Amount': amount, 'Date': date}, ignore_index=True)

# # Define a function to calculate the user's total income and expenses
# def calculate_total():
#     global df
#     income = df[df['Type'] == 'Income']['Amount'].sum()
#     expenses = df[df['Type'] == 'Expense']['Amount'].sum()
#     total = income - expenses
#     return total

# # Define a function to provide insights into the user's spending habits
# def get_insights():
#     global df
#     expenses_by_type = df[df['Type'] == 'Expense'].groupby('Type').sum()
#     expenses_by_date = df[df['Type'] == 'Expense'].groupby('Date').sum()
#     print('Expenses by type:\n', expenses_by_type)
#     print('Expenses by date:\n', expenses_by_date)

# # Test the program
# add_transaction('Income', 5000, '2022-03-01')
# add_transaction('Expense', 2000, '2022-03-02')
# add_transaction('Expense', 3000, '2022-03-03')
# add_transaction('Expense', 1000, '2022-03-04')
# total = calculate_total()
# print('Total income and expenses:', total)
# get_insights()


import pandas as pd

# Create an empty DataFrame to store income and expenses
df = pd.DataFrame(columns=['Type', 'Amount', 'Date'])

# Define a function to add income or expenses to the DataFrame
def add_transaction(transaction_type, amount, date):
    global df
    new_transaction = pd.DataFrame({'Type': [transaction_type], 'Amount': [amount], 'Date': [date]})
    df = pd.concat([df, new_transaction], ignore_index=True)

# Define a function to calculate the user's total income and expenses
def calculate_total():
    global df
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expenses = df[df['Type'] == 'Expense']['Amount'].sum()
    total = income - expenses
    return total

# Define a function to provide insights into the user's spending habits
def get_insights():
    global df
    expenses_by_type = df[df['Type'] == 'Expense'].groupby('Type').sum()
    expenses_by_date = df[df['Type'] == 'Expense'].groupby('Date').sum()
    print('Expenses by type:\n', expenses_by_type)
    print('Expenses by date:\n', expenses_by_date)

# Test the program
add_transaction('Income', 5000, '2022-03-01')
add_transaction('Expense', 2000, '2022-03-02')
add_transaction('Expense', 3000, '2022-03-03')
add_transaction('Expense', 1000, '2022-03-04')
total = calculate_total()
print('Total income and expenses:', total)
get_insights()
