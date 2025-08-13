
'''
ATM Withdrawal Simulator
Imagine you’re building a backend feature for an ATM. Customers can request multiple withdrawals during one session. 
Your task is to simulate how the system should handle each request based on the account balance.
Tasks:
Use a while loop to iterate through the list named withdrawals.
For every withdrawal:
If the current balance is enough:
Subtract the amount.
Append a success message: "Withdrawn: {amount}"
If not enough:
Append a message: "Insufficient funds for requested amount: {amount}"
After all withdrawals:
Append the final balance as: "Remaining Balance: balance"
Return a list containing all the messages.
'''

# This function will be tested automatically. 
# Do not change the function name or parameters.
def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    messages = []
    i = 0
    while i < len(withdrawals):
        amount = withdrawals[i]
        if balance >= amount:
            balance -= amount
            messages.append(f"Withdrawn: {amount}")
        else:
            messages.append(f"Insufficient funds for requested amount: {amount}")
        i += 1
        
    messages.append(f"Remaining Balance: {balance}")
    return messages

